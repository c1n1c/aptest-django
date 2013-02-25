aptest-django
=============

simple demo app

create test environment by buildout:

  python bootstrap.py
  bin/buildout

create test db:

  bin/django syncdb
  bin/django loaddata fixtures/test-pages.json

run test server:

  bin/django runserver
