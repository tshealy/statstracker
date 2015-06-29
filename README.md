# Project Structure

Models are implemented as follows:

 - User: built-in model from Django for login accounts
 - Profile: dual model to User, used to establish relationships with other models
   + Has a set of activities associated with it
 - Activity: Something that is counted by-day
   + Has a set of stats associated with it
 - Stat: The count of the activity on a given day

App structure:

 - activities
 - users
 - api

API urls:

 - /activities/{id}
   + can perform an action on a single activity
 - /activities/{id}/stats/
   + can perform an action on all activity's stats at once
 - /stats/{id}

## Location of Templates

These are important for the front-end people to know.

 - Main index: /statstracker/templates/index.html
 - Login page: /statstracker/users/templates/users/registration/login.html
 - Registration page: /statstracker/users/templates/users/register.html

## Requirements

When doing so manually, requirements should be installed as:

    pip3 install -r dev_requirements.txt

# Welcome to your new Django single-page app project!

This template will ease your way in building a single-page app backed by a Django API.

To use this template, run:

```
django-admin.py startproject YOUR_PROJECT_NAME --template=https://github.com/tiyd-python-2015-05/single-page-app-template/archive/master.zip --extension=py,md --name=Procfile
```

Change YOUR_PROJECT_NAME before running the above.

## Files you should know about

* `statstracker/templates/index.html` - This is where all your HTML should go. It has a few funny things in there. Make sure to use `\{% static "path/to/file.css" %\}` for all links to static files.

* `statstracker/static/` - All your static files go here. You can write them by hand or generate them with gulp or another tool.

## Heroku instructions

This app should work well with Heroku as long as you run the following commands:

```
heroku config:set DJANGO_SETTINGS_MODULE=statstracker.heroku_settings
heroku config:set PYTHONPATH=statstracker
heroku config:set SECRET_KEY=$(date | md5 | base64)
```
