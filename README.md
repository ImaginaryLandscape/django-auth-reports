
Django Auth Reports
===================

A Django application that:
-Adds csv downloads of group permissions
-Adds right-side filtering in m2m filter_horizontal widgets


Installation
============

    $ pip install django-auth-reports

Add the following to the top of the INSTALLED_APPS in your project's settings file, above django.contrib.admin and django.contrib auth:

    'auth_reports',

Collect static media:

   ``manage.py collectstatic``
