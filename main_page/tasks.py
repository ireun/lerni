from __future__ import absolute_import
import celery
import subprocess

from main_page.models import (
    DBSession,
    PingResults,
    PingIPs)
import transaction


@celery.task
def task(x, y):
    return x + y


@celery.task
def ping():
    session = DBSession()
    for host in DBSession.query(PingIPs):
        res = subprocess.call(['ping', '-c', '3', host.ip])
        if res == 0:
            session.add(PingResults(host.id, True))
        else:
            session.add(PingResults(host.id, False))
    transaction.commit()
