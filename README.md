[Lerni](http://lerni.info/) - Modern CMS for schools.
==================================================

Contribution Guides
--------------------------------------
Lerni is open source software, every contribution would be great.
Please be sure to read current TODO and general overview before you jump into writing code.

1. [Current TODO](http://docs.lerni.info/todo)
2. [General Overview](http://docs.lerni.info/overview

Use Lerni on your own computer
--------------------------------------
### Instalation on Ubuntu 13.04

First, install all required packages
```bash
sudo apt-get install python-setuptools python-dev build-essential gnupg python-virtualenv
sudo apt-get install wkhtmltopdf xvfb xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
sudo easy_install virtualenv
```
Clone this repository
```bash
git clone https://github.com/kamilx3/lerni.git
```
To test if everything works fine download sample initialization data set.
```bash
git submodule update --init
```
Create new python virtual environment.
```bash
virtualenv --no-site-packages lernienv
source lernienv/bin/activate
```
cd <directory containing this file>
```bash
cd lerni
```
Develop the project.
```bash
$venv/bin/python setup.py develop
```
Initialize testing database.
```bash
$venv/bin/initialize_main_page_db development.ini
```
And finally the application.
```bash
$venv/bin/pserve development.ini
```