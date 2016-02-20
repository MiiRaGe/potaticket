
# Potato Backend Developer Test

[![Build Status](https://travis-ci.org/MiiRaGe/potaticket.svg?branch=master)](https://travis-ci.org/MiiRaGe/potaticket)

[![Coverage Status](https://coveralls.io/repos/github/MiiRaGe/potaticket/badge.svg?branch=master)](https://coveralls.io/github/MiiRaGe/potaticket?branch=master)

This is a basic Django project which is designed to provide you with a few challenges to demonstrate your ability.

The application is a ticketing application. It stores tickets within projects and allows users to be assigned to these tickets.

Please fix the bugs and implement the features listed below.

Ensure that your code is committed with meaningful commit messages; show your working.

When you are finished please provide us with a URL to a repository where we can check out your code.

## Setup

- Run `./install_deps` (this will pip install requirements, and download the App Engine SDK)
- `python manage.py loaddata site`
- `python manage.py runserver`

The application is written using the [Djangae](http://djangae.readthedocs.org/en/latest/) project

## Tasks - bugs

- Update a ticket - an internal server error occurs
- It is possible to move a ticket from one project to another by altering the URL on the edit ticket page. This should not be allowed
- Tickets with long descriptions break the layout

## Tasks - new features

- On the ticket list page if there are no tickets show "No tickets have been created for this project"
- On the ticket list page if there are no users assigned to a ticket show "No assigned users" in the "assigned" field
- On the project list page, add a new column showing the count of how many tickets there are in each project
- On the project list page, projects that the user has assigned tickets on should be shown above the other projects
- In the edit ticket page show only the email address of each user in the "Assignees" input
- Add the ability to delete tickets
- Improve the multiselect for assignees on the edit ticket page. Consider using a library such as [Chosen](http://harvesthq.github.io/chosen/) to help with this
- Add a watch task to the default gulp task so that changes to any of the SCSS files result in the CSS files being updated


## Bonus tasks

If you feel like carrying on improving this application, please do!

The following consistency task is one that you might like to have a look at.

### Eventual consistency

Pages seem to need a refresh after updating an object in the application

This is due to the fact that the Google App Engine datastore is an 'eventually consistant' database. Once an entity is saved some data retrieval operations may not immediately reflect this change. To read more about this see the Google App Engine [Datastore](https://cloud.google.com/appengine/docs/python/datastore/) documentation.

Can you create a solution to solve this problem?  There is no right or wrong solution.

## Side tasks

- Upgraded to django 1.8
- Added config file to check for pep8:

    - ```py.test --pep8```

- Added clickable link for accessing project detail in project list.
- Added continuous integration and coverage (with travis-ci and coveralls respectively).
- travis-ci also deploys to google app engine when build passes
