# -*- coding: utf-8 -*-
import contextlib
import io
import os
import sys
from typing import Dict
from contextlib import redirect_stdout

from celery import Celery, states
from celery.utils.log import get_task_logger
from behave.__main__ import main as behave_main

app = Celery("tasks", broker="redis://redis@redis:6379//")
app.conf.task_default_queue = "behave"
app.conf.broker_transport_options = {'visibility_timeout': 3600}
app.conf.send_events = True
app.conf.send_task_sent_event = True

REPLACE_CHARS = ("Scenario: ", "Scenario Outline: ", "\r")

logger = get_task_logger(__name__)


@contextlib.contextmanager
def set_env(environ: Dict[str, str]):
    """Temporarily set the process environment variables.

    SRC: https://stackoverflow.com/a/34333710
    """
    old_environ = dict(os.environ)
    os.environ.update(environ)
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(old_environ)


@app.task(
    bind=True,
    autoretry_for=(),
    broker_pool_limit=1,
    ignore_result=True,
    name="run scenario",
    queue="behave",
)
def delegate_test(self, browser: str, scenario: str):
    def replace_char(string: str) -> str:
        for chars in REPLACE_CHARS:
            string = string.replace(chars, "")
        return string

    args_list = [
        "features/",
        "--no-skipped",
        "--format=allure_behave.formatter:AllureFormatter",
        f"--outfile={browser}_results/",
        "--logging-filter=-root",
        "--name",
        replace_char(scenario),
    ]

    # set env var that decides in which browser the test should be executed
    env_vars = {
        "BROWSER": browser,
        "ALLURE_INDENT_OUTPUT": "2"
    }
    with set_env(env_vars):
        temp_redirect = io.StringIO()
        with redirect_stdout(temp_redirect):
            exit_code = behave_main(args_list)

    behave_result = temp_redirect.getvalue()
    logger.info(behave_result)
    if exit_code == 1:
        self.update_state(state=states.FAILURE, meta=behave_result)
    sys.exit(exit_code)
