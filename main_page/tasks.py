from __future__ import absolute_import
from celery.task import Task
from celery.task import task
from celery import Celery

from .models import (
    DBSession,
    TaskItem,
)

import time
import random

#app = Celery('main_page.tasks', backend='redis://', broker='amqp://')

@task(name='task')
def task(x, y):
    return x + y