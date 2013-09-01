lerni     
=====

Modern CMS for schools.

Getting Started
---------------
- sudo apt-get install python-setuptools python-dev build-essential gnupg python-virtualenv
- sudo apt-get install wkhtmltopdf xvfb xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
- install modified version of python-wkhtmltopdf from https://github.com/rlau/python-wkhtmltopdf.git

- cd <directory containing this file>
- $venv/bin/python setup.py develop
- $venv/bin/initialize_main_page_db development.ini
- $venv/bin/pserve development.ini
