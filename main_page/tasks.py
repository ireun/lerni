from __future__ import absolute_import
import celery
import subprocess

from main_page.models import (
    DBSession,
    PingResults,
    PingIPs,
    Settings)
import transaction


@celery.task
def task(x, y):
    return x + y


@celery.task
def ping():
    try:
        history = DBSession.query(Settings).filter_by(name="services_availability_history").first().value
    except AttributeError:
        history = False
    session = DBSession()
    for host in DBSession.query(PingIPs):
        res = subprocess.call(['ping', '-c', '3', host.ip])
        if not history:
            for x in DBSession.query(PingResults).filter_by(ip_id=host.id):
                session.delete(x)
        if res == 0:
            session.add(PingResults(host.id, True))
        else:
            session.add(PingResults(host.id, False))
    transaction.commit()
