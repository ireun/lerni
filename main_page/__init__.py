from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from main_page.security import groupfinder

from sqlalchemy import engine_from_config
from .models import DBSession
from pyramid.renderers import JSONP
from pyramid.httpexceptions import HTTPNotFound
from pyramid_mailer.mailer import Mailer
from webassets import Bundle
from pyramid_webassets import get_webassets_env
import os
extra_environ = {'HTTP_X_REQUESTED_WITH' : 'XMLHttpRequest'}

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder, hashalg='sha512', timeout=60*60*24*7)  ## Change it
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings, root_factory='main_page.models.RootFactory')
    config.include('pyramid_mailer')
    config.registry['mailer'] = Mailer.from_settings(settings)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    #config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('assets', 'assets', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('radio','/radio')


    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('register', '/register')
    config.add_route('forgot_password', '/forgot-password')
    config.add_route('activate_account', '/activate-account')

    config.add_route('zastepstwa', '/zastepstwa')
    config.add_renderer('jsonp', JSONP(param_name='callback'))
    config.add_route('jsonp_post_comments', '/api/jsonp/post_comments')
    config.add_route('jsonp_year_add', '/api/jsonp/year/add') #articles zrobic podobnie#
    config.add_route('jsonp_year', '/api/jsonp/year/{year}')
    config.add_route('jsonp_people', '/api/jsonp/people')
    config.add_route('jsonp_groups', '/api/jsonp/groups')
    config.add_route('jsonp_mobile_login', '/api/jsonp/mobile_login')

    config.add_route('user_list','/api/jsonp/user-list')
    config.add_route('delete_user','/api/jsonp/delete-user')
    config.add_route('update_user','/api/jsonp/update-user')
    config.add_route('create_user','/api/jsonp/create-user')

    config.add_route('timetable_list','/api/jsonp/timetable-list')
    config.add_route('delete_timetable','/api/jsonp/delete-timetable')
    config.add_route('update_timetable','/api/jsonp/update-timetable')
    config.add_route('create_timetable','/api/jsonp/create-timetable')

    config.add_route('lesson_list','/api/jsonp/lesson-list')
    config.add_route('delete_lesson','/api/jsonp/delete-lesson')
    config.add_route('update_lesson','/api/jsonp/update-lesson')
    config.add_route('create_lesson','/api/jsonp/create-lesson')
    config.add_route('options_teacher_list','/api/jsonp/options-teacher-list')
    config.add_route('options_subjects_list','/api/jsonp/options-subjects-list')
    config.add_route('options_groups_list','/api/jsonp/options-groups-list/{term_id}')

    config.add_route('folder_list','/api/jsonp/folder-list')
    config.add_route('delete_folder','/api/jsonp/delete-folder')
    config.add_route('update_folder','/api/jsonp/update-folder')
    config.add_route('create_folder','/api/jsonp/create-folder')
    config.add_route('options_folders_list','/api/jsonp/options-folders-list')
    config.add_route('options_folders_css_list','/api/jsonp/options-folders-css-list')
    config.add_route('entry_list','/api/jsonp/entry-list')
    config.add_route('delete_entry','/api/jsonp/delete-entry')
    config.add_route('update_entry','/api/jsonp/update-entry')
    config.add_route('create_entry','/api/jsonp/create-entry')
    config.add_route('options_entries_css_list','/api/jsonp/options-entries-css-list')


    config.add_route('jsonp_system_info', '/api/jsonp/system_info')

    config.add_route('view_page', '/p/{pagename}')
    config.add_route('page', '/p/{pagename}/{subname}')
    config.add_route('edit_page', '/p_edit/{pagename}')



    config.add_route('admin', '/admin')
    config.add_route('admin_overview', '/admin/overview')
    config.add_route('admin_articles', '/admin/articles')
    config.add_route('admin_articles_add', '/admin/articles/add')
    config.add_route('admin_users', '/admin/users')
    config.add_route('admin_people', '/admin/teachers')
    config.add_route('admin_personel', '/admin/personel')
    config.add_route('admin_support', '/admin/support')
    config.add_route('admin_students', '/admin/students')
    config.add_route('admin_others', '/admin/others')
    config.add_route('admin_log_years', '/admin/log/years')
    config.add_route('admin_log_years_groups', '/admin/log/years/groups/{year}')
    config.add_route('admin_log_years_groups_students', '/admin/log/years/groups/{year}/{group}')
    config.add_route('admin_log_timetables', '/admin/log/timetables')
    config.add_route('admin_log_timetables_edit', '/admin/log/timetables/edit')

    config.add_route('admin_layouts', '/admin/layouts')

    config.add_route('admin_substitutions', '/admin/substitutions')
    config.add_route('admin_substitutions_add', '/admin/substitutions/add')
    config.add_route('admin_substitutions_view', '/admin/substitutions_view/{id}')
    config.add_route('admin_substitutions_edit', '/admin/substitutions_edit/{id}')
    config.add_route('admin_substitutions_del', '/admin/substitutions_del/{id}')
    config.add_route('admin_lucky_number','/admin/lucky-number')

    config.add_route('account_folders', '/account/folders')
    config.add_route('account_entries', '/account/entries')
    config.add_route('account_presentations', '/account/presentations')
    config.add_route('account_tasks_sets', '/account/tasks-sets')
    config.add_route('account_questions_sets', '/account/questions-sets')
    config.add_route('account_other', '/account/other')
    config.add_route('account', '/account')
    config.add_route('phone_app', '/account/phone')

    config.add_route('support', '/support')
    config.add_route('support_services', '/support/services')
    config.add_route('support_ask', '/support/ask')
    config.add_route('support_ask_ticket', '/support/ticket-{id}')
    config.add_route('support_faq', '/support/faq')


    config.add_route('successes', '/nasze-sukcesy')
    config.add_route('successes_gim', '/nasze-sukcesy/gimnazjum')
    config.add_route('successes_lic', '/nasze-sukcesy/liceum')
    config.add_route('graduates', '/absolwenci')

    config.add_route('companionship', '/partnerzy')

    config.add_route('gallery', '/galeria')

    config.add_route('admin_gallery', '/admin/gallery')
    config.add_route('file_upload', '/file-upload')


    config.add_route('connection', '/connection')

    config.add_route('loading', '/loading')
    config.add_route('entries', '/entries')
    config.add_route('entry_save', '/entry/save')
    config.add_route('entry', '/entry/{id}')
    config.add_route('folder', '/folder/{id}')
    config.add_route('presentations', '/presentations')
    config.add_route('presentation', '/presentation/{id}')
    config.add_route('set', '/set/{id}')

    config.add_route('user','/u/{user_name}')

    config.add_route('lucky', '/sis/lucky')
    config.add_route('sis_home', '/sis')
    config.add_route('sis_about', '/sis/about')
    config.add_route('schedule', '/sis/schedule')

    config.add_route('easy_link', '/{link}')

    for x in os.walk("main_page/static/src/"):
        for y in x:
            for z in y:
                if z[-7:]==".min.js":
                    name=x[0][21:]+"/"+z
                    print Bundle("src/"+name, output=name, filters=['closure_js']).urls(get_webassets_env(config))
                if z[-3:]==".js":
                    name=x[0][21:]+"/"+z
                    print Bundle("src/"+name, output=name[:-3]+".min.js", filters=['closure_js']).urls(get_webassets_env(config))
    for x in os.walk("main_page/static/src/"):
        for y in x:
            for z in y:
                if z[-4:]==".css":
                    name=x[0][21:]+"/"+z
                    print Bundle("src/"+name, output=name[:-4]+".min.css").urls(get_webassets_env(config)) #, filters=['cssmin']
    #scroll_up_css=Bundle("libs/scrollup/themes/pill.css")
    #scroll_up_js=Bundle("libs/scrollup/jquery.scrollUp.min.js","js/scroll_up.js")

    #diagrams=Bundle("libs/raphael/raphael-min.js","libs/jquery.browser/jquery.browser.js","js/diagrams.js")
    #noisy_js=Bundle("js/noisy.js")
    #content_js=Bundle("js/content.js") ## bonzo (?)
    #content_css=Bundle("css/content.css","css/entries.css")
    #spoiler_js=Bundle("libs/spoiler/spoiler.js","js/spoiler.js")

    #easteregg_js=Bundle('libs/easter/easter.js')  #easter_egg
    #gravity = Bundle('libs/easter/gravity/jGravity.js')  #does not work properly

    #c_css = Bundle(scroll_up_css, owl_css, content_css, social_css, raptor_css, output='gen/content.min.css',  debug=False)

    #r_js = Bundle(cookie_js, bootstrap_js, owl_js, time_js, fit_vids_js, flickr_js, base_js, holder_js, progression_js, 'js/form_login.js', output='gen/main.min.js', debug=False)
    #r_css =  Bundle(bootstrap_css, cookie_css, owl_css, base_css,progression_css, output='gen/main.min.css', debug=False)

    config.include('pyramid_rewrite')
    config.add_rewrite_rule(r'/(?P<path>.*)/', r'/%(path)s')
    config.scan()
    return config.make_wsgi_app()

