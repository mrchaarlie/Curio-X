This is Curio.
=====

University of Waterloo
Systems Design Engineering, 4th year Design Project

Project Members:
Charles Wu, Jonathan Johnston, Robert Bon, Kenneth Chan

Project Supervisor:
Professor Edith Law

---

Developing a generalized and gamified crowd-sourcing platform for collecting scientific research data from images.

---

### Creating a virtualenv and installing Django

In order to run the project, you'll need to install Django using the python package installer pip (the easiest way). The most simple way to do this without installing packages in your root is to create a virtual environment with virtualenv, activate it, and install the packages you require.

```
sudo apt-get install python-pip
sudo pip install virtualenv
virtualenv -p /usr/bin/python3 curiox
source curiox/bin/activate

pip install django==1.7.2
pip install simplejson
```

### Running the development server

We're using Django as our web framework, so when doing development you can run Django in development mode. You will need to be running a current version of Python 3.x:

```
python manage.py runserver
```

Go to where the dev server is hosted:

```
localhost:8000/game/index
```

The administrator login is admin:admin.

### Running production

Currently, we have:
* Load default username bases (adjectives and animals; ex. CuriousBear) to the database
* Load password bases (random selection of 2K or 11K words)

```
python manage.py loadwords --adjectives static/lists/adjectivelist.csv --animals static/lists/animallist.csv
python manage.py loadwords --words static/lists/shortwordlist.csv
```

* Run a model migration to initialize the database

```
python manage.py makemigrations game
python manage.py sqlmigrate game <number> #optional
python manage.py migrate
```

* Load image URLs and their metadata into the database

```
python manage.py loadimages --images=static/lists/fewobj_images.csv
python manage.py loadimages --images=static/lists/manyobj_images.csv
```

* Backing up and restoring SQLite database

```
sudo apt-get install sqlite3
sqlite3 db.sqlite3 ".backup db.backup" # create a backup
```

* Uploading backup to S3
* Will first need to get s3cmd at http://s3tools.org/download

```
s3cmd --configure #configure to your S3 bucket
s3cmd put db.backup s3://curiox/backups/db.backup.<month>.<day> #follow some convention
```

#### Logging

Code-level logging outputs to 'log' in the base directory. Logging options are specified in the settings.py file. To log in a python file, do the following:

```
import logging

logger = logging.getLogger()

#...
logger.debug('I can see this debug message in the log file')
#...
```

#### Configuring Apache

This section is unfinished.

Install Apache, check the version number (2.4.x) and enable the VirtualHost by creating a new site 'curiox'

```
sudo apt-get install apache2
apache2 -v   #get version
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/curiox.conf
```

Add to the /etc/apache2/apache2.conf file

```
ServerName localhost
```

Another server might be listening on the port 80, so you can either change the port in /etc/apache2/ports.conf, or

```
sudo netstat -ltnp | grep :80
kill <pid>
```

Enable the site and start Apache and check out the default Apache page at 'localhost'

```
sudo a2ensite curiox
sudo service apache2 restart
```

Now, to host Python applications with Apache, we will need a module that runs with Apache called mod\_wsgi, so let's install that

```
sudo apt-get install libapache2-mod-wsgi
```
