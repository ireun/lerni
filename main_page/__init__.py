from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from main_page.security import groupfinder

from sqlalchemy import engine_from_config
from .models import DBSession
from pyramid.renderers import JSONP
from pyramid.httpexceptions import HTTPNotFound
from pyramid_mailer.mailer import Mailer

extra_environ = {'HTTP_X_REQUESTED_WITH' : 'XMLHttpRequest'}

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder)  ## Change it
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings, root_factory='main_page.models.RootFactory')
    config.include('pyramid_mailer')
    config.registry['mailer'] = Mailer.from_settings(settings)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('assets', 'assets', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('register', '/register')
    config.add_route('zastepstwa', '/zastepstwa/')
    config.add_route('captcha', '/captcha/{hashcode}')
    config.add_route('captcha_validate', '/captcha/validate/{hashcode}')
    config.add_renderer('jsonp', JSONP(param_name='callback'))
    config.add_route('jsonp_post_comments', '/api/jsonp/post_comments')
    config.add_route('add_comment', '/add_comment')
    config.add_route('rm_comment', '/rm_comment')
    config.add_route('jsonp_people', '/api/jsonp/people')
    config.add_route('jsonp_groups', '/api/jsonp/groups')
    config.add_route('jsonp_mobile_login', '/api/jsonp/mobile_login')
    
    config.add_route('view_page', '/p/{pagename}')
    config.add_route('page', '/p/{pagename}/{subname}')
    config.add_route('edit_page', '/p_edit/{pagename}')
    
    
    config.add_route('plan', '/plan')
    config.add_route('admin', '/admin')
    config.add_route('admin_overview', '/admin/overview')
    config.add_route('admin_articles', '/admin/articles')
    config.add_route('admin_articles_add', '/admin/articles/add')
    config.add_route('admin_people', '/admin/people')
    config.add_route('ram_usage', '/admin/overview/ram_usage')
    config.add_route('admin_substitutions', '/admin/substitutions')
    config.add_route('admin_substitutions_add', '/admin/substitutions/add')
    config.add_route('admin_substitutions_view', '/admin/substitutions_view/{id}')
    config.add_route('admin_substitutions_edit', '/admin/substitutions_edit/{id}')
    config.add_route('admin_substitutions_del', '/admin/substitutions_del/{id}')
    config.add_route('admin_lucky_number','/admin/lucky-number')
    
    config.add_route('account', '/account')
    config.add_route('phone_app', '/account/phone')
    
    config.add_route('support', '/support')
    config.add_route('support_services', '/support/services')
    config.add_route('support_stats', '/support/stats')
    config.add_route('support_ask', '/support/ask')
    config.add_route('support_ask_ticket', '/support/ticket-{id}')
    config.add_route('support_faq', '/support/faq')
    
    
    config.add_route('successes', '/nasze-sukcesy')
    config.add_route('successes_gim', '/nasze-sukcesy/gimnazjum')
    config.add_route('successes_lic', '/nasze-sukcesy/liceum')
    config.add_route('graduates', '/absolwenci')

    config.add_route('companionship', '/partnerzy')
    config.add_route('contact', '/kontakt')
    config.add_route('books', '/podreczniki')
    config.add_route('competitions', '/konkursy')

    config.add_route('gallery', '/galeria')
    
    config.add_route('admin_gallery', '/admin/gallery')
    config.add_route('file_upload', '/file-upload')

    
    config.add_route('connection', '/connection')
    config.add_notfound_view(notfound, append_slash=True)
    config.scan()
    return config.make_wsgi_app()
    
def notfound(request):
    return HTTPNotFound('Not found, bro.')
