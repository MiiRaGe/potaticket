
# Potaticket (Developper test)

[![Build Status](https://travis-ci.org/MiiRaGe/potaticket.svg?branch=master)](https://travis-ci.org/MiiRaGe/potaticket)

[![Coverage Status](https://coveralls.io/repos/github/MiiRaGe/potaticket/badge.svg?branch=master)](https://coveralls.io/github/MiiRaGe/potaticket?branch=master)

This project was a technical test for a job application, starting from a skeleton project with bugs the goal was to fix them.

The bug fixing and extra features were done over a weekend.

## Tasks - bugs

- FIXED: Update a ticket - an internal server error occurs
- FIXED: It is possible to move a ticket from one project to another by altering the URL on the edit ticket page. This should not be allowed
- FIXED: Tickets with long descriptions break the layout

## Tasks - new features

- DONE: On the ticket list page if there are no tickets show "No tickets have been created for this project"
- DONE: On the ticket list page if there are no users assigned to a ticket show "No assigned users" in the "assigned" field
- DONE: On the project list page, add a new column showing the count of how many tickets there are in each project
- DONE: On the project list page, projects that the user has assigned tickets on should be shown above the other projects
- DONE: In the edit ticket page show only the email address of each user in the "Assignees" input
- DONE: Add the ability to delete tickets
- DONE: Improve the multiselect for assignees on the edit ticket page. Consider using a library such as [Chosen](http://harvesthq.github.io/chosen/) to help with this
- DONE: Add a watch task to the default gulp task so that changes to any of the SCSS files result in the CSS files being updated

## Side tasks

- Upgraded to django 1.8 LTS
- Added config file to check for pep8:

    - ```py.test --pep8 -m pep8 tracker```

- Added clickable link for accessing project detail in project list.
- Added continuous integration and coverage (with travis-ci and coveralls respectively).
- travis-ci also deploys to google app engine when build passes
