import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
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
    'pdfkit'
    ]

setup(name='main_page',
      version='0.0',
      description='main_page',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='main_page',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = main_page:main
      [console_scripts]
      initialize_main_page_db = main_page.scripts.initializedb:main
      """,
      )
