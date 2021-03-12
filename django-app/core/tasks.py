from core.celery import app
from time import sleep


@app.task
def hello_world():
    print('Begin from Celery !!!!!!!!')
    sleep(10)  # deley 10 sec.
    print('Hi from Celery !!!!!!!!')
