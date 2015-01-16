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

```virtualenv -p /usr/bin/python3 curiox
source py3env/bin/activate
pip install django
```

### Running the development server

We're using Django as our web framework, so when doing development you can run Django in development mode. You will need to be running a current version of Python 3.x:

```python manage.py runserver```
