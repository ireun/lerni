# -*- coding: utf-8 -*-
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
import locale
from sqlalchemy import desc    ######################################
from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    has_permission,
    )
from main_page.models import (DBSession,
                              People)


def groupfinder(username, request):
    user = DBSession.query(People).filter_by(email=username).first()
    if user:
        print ['g:%s' % g.group.name for g in user.groups]
        return ['g:%s' % g.group.name for g in user.groups]
    else:
        return ['g:unregistered']