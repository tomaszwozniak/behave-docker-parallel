from celery import Celery
from behave.__main__ import main as behave_main

app = Celery('tasks', broker='pyamqp://rabbitmq:rabbitmq@rabbit1//')
app.conf.task_default_queue = 'behave'


@app.task
def delegate_test(scenario):
    argstable = ['behave/features/django_admin/users_crud.feature', '-n{}'.format(scenario), '-f allure_behave.formatter:AllureFormatter', '-o%allure_result_folder%']
    print(argstable)
    behave_main(argstable)
    return
