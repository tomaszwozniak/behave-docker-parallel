# -*- coding: utf-8 -*-
import contextlib
import os
import sys
from typing import Dict

from celery import Celery, states
from behave.__main__ import main as behave_main

from io import StringIO

app = Celery("tasks", broker="redis://redis@redis:6379//")
app.conf.task_default_queue = "behave"
app.conf.broker_transport_options = {'visibility_timeout': 3600}
app.conf.send_events = True
app.conf.send_task_sent_event = True

REPLACE_CHARS = ("Scenario: ", "Scenario Outline: ", "\r")


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
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 3},
    retry_backoff=10,
    broker_pool_limit=None,
)
def delegate_test(self, browser: str, scenario: str):
    def replace_char(string: str) -> str:
        for chars in REPLACE_CHARS:
            string = string.replace(chars, "")
        return string

    argstable = [
        "behave/features/django_admin/",
        "--no-skipped",
        "--format",
        "pretty",
        # disable allure reports for now as hundreds of unnecessary json
        # reports are being generated
        #'--format', 'allure',
        #'--outfile', 'allure_results',
        "--logging-filter=-root",
        "--name",
        replace_char(scenario),
    ]

    old_stdout = sys.stdout
    io = StringIO()
    sys.stdout = io

    # set env var that decides in which browser the test should be executed
    with set_env({"BROWSER": browser}):
        behave_main(argstable)

    sys.stdout = old_stdout
    behave_result = io.getvalue()

    if "1 scenario passed" not in behave_result:
        # manually update the task state
        self.update_state(state=states.FAILURE, meta=behave_result)

        raise Exception(behave_result)
    return "Pass"

