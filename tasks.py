from celery import Celery
from behave.__main__ import main as behave_main

app = Celery('tasks', broker='pyamqp://rabbitmq:rabbitmq@rabbit1//')
app.conf.task_default_queue = 'behave'
app.conf.send_events = True
app.conf.send_task_sent_event = True


@app.task
def delegate_test(scenario):
    argstable = [
        'behave/features/django_admin/',
        '-n{}'.format(scenario.replace('Scenario: ', '').replace('\r', '')),
        '-f allure_behave.formatter:AllureFormatter',
        '-o%allure_result_folder%']
    behave_main(argstable)
    return scenario
