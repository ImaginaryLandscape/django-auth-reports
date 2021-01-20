
Django Auth Reports
===================

A Django application that:  
-Adds csv downloads of group permissions  
-Adds right-side filtering in m2m filter_horizontal widgets

Compatibility
=============

For Django 1.x, use django-auth-reports 1.x

For Django 2.x, use django-auth-reports 2.x

Installation
============

    $ pip install django-auth-reports

Add the following to the top of the INSTALLED_APPS in your project's settings file, above django.contrib.admin and django.contrib auth:

    'auth_reports',

Collect static media:

   ``manage.py collectstatic``
