import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

dependency_links = [
    'https://github.com/jpunwin/pyramid_celery/tarball/master#egg=pyramid_celery-1.3'
]

requires = [
    'pyramid',
    'pyramid_mako',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'pyramid-mailer',
    'psutil',
    'itsdangerous',
    'recaptcha-client',
    'python-gnupg',
    'BeautifulSoup',
    'TransmissionClient',
    'pyramid_rewrite',
    'pyramid_webassets',
    'pyscss',
    'closure',
    'cssmin',
    'bbcode',
    'xmpppy',
    'pdfkit',
    #Anki requipments
    'send2trash',
    'httplib2',
    'pyaml',
    'flickrapi',
    'pyramid_celery==1.3',
    'redis',
    'mysql-python',
    'python-irclib'] ##Yup, you have to install paver, hgtools manualy first.

setup(name='main_page',
      version='0.1',
      description='main_page',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"],
      author='Kamil Danak',
      author_email='kamilx3@gmail.com',
      url='http://lerni.info',
      keywords='lerni web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='main_page',
      install_requires=requires,
      dependency_links=dependency_links,
      entry_points={
          'paste.app_factory': [
              'main = main_page:main',
          ],
          'console_scripts': [
              'initialize_main_page_db = main_page.scripts.initializedb:main',
              'ircbot = main_page.scripts.ircbot:main',
          ]}
)
