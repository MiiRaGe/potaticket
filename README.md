
# Potaticket (Developper test)

[![Build Status](https://travis-ci.org/MiiRaGe/potaticket.svg?branch=master)](https://travis-ci.org/MiiRaGe/potaticket)

[![Coverage Status](https://coveralls.io/repos/github/MiiRaGe/potaticket/badge.svg?branch=master)](https://coveralls.io/github/MiiRaGe/potaticket?branch=master)

Here's what I managed to do over the weekend.

I'm not super happy about the responsiveness of the website, especially for super long title, truncate doesn't look like the right solution

## Tasks - bugs

FIXED - Update a ticket - an internal server error occurs
FIXED - It is possible to move a ticket from one project to another by altering the URL on the edit ticket page. This should not be allowed
FIXED - Tickets with long descriptions break the layout

## Tasks - new features

DONE - On the ticket list page if there are no tickets show "No tickets have been created for this project"
DONE - On the ticket list page if there are no users assigned to a ticket show "No assigned users" in the "assigned" field
DONE - On the project list page, add a new column showing the count of how many tickets there are in each project
DONE - On the project list page, projects that the user has assigned tickets on should be shown above the other projects
DONE - In the edit ticket page show only the email address of each user in the "Assignees" input
DONE - Add the ability to delete tickets
DONE - Improve the multiselect for assignees on the edit ticket page. Consider using a library such as [Chosen](http://harvesthq.github.io/chosen/) to help with this
DONE - Add a watch task to the default gulp task so that changes to any of the SCSS files result in the CSS files being updated


## Bonus tasks

I haven't had time to look at that, however this is really intriging and I didn't know it would be so obvious when updating things.

## Side tasks

- Upgraded to django 1.8 LTS
- Added config file to check for pep8:

    - ```py.test --pep8 -m pep8 tracker```

- Added clickable link for accessing project detail in project list.
- Added continuous integration and coverage (with travis-ci and coveralls respectively).
- travis-ci also deploys to google app engine when build passes
