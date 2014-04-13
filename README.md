Overview
========

A Django Registration app to be used for online user registration for "Introduction to Python" workshop.

Quick Start
-----------

You should be able to get started with:

    $ git clone git@github.com:sourabhv/pygameWorkshopRegistration.git
    $ cd pygameWorkshopRegistration 
    
    # configure your database (sample here- https://dpaste.de/ej1d )
    $ vim pygameWorkshopRegistration/settings/local.py

    # start the django server
    $ python manage.py runserver

Developing
----------

If you wish to contribute to pygameWorkshopRegistration, please create a
**fork** of this repository and work on your version and then send us a pull request.

One more thing, do setup an upstream to the original repository so that you're
always updated with the latest code.

    $ git add remote upstream
    git@github.com:sourabhv/pygameWorkshopRegistration.git

Next, please follow the following everytime before you start working

    $ git fetch upstream
    $ git checkout master
    $ git merge upstream/master

Happy hacking!
