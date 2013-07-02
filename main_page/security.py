# -*- coding: utf-8 -*-
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
import locale
from sqlalchemy import desc    ######################################
from main_page.models import (
    DBSession,
    MenuTop,
    MenuLeft,
    Articles,
    Users_Groups,
    Substitutions,
    Absent,
    Replace,
    People,
    Lessons,
    Groups,
    Duty,
    Shift,
    Places,
    )
    
def groupfinder(username, request):
    group_id = DBSession.query(People).filter_by(login=username).first().group_id
    return [DBSession.query(Users_Groups).filter_by(id=group_id).first().name]