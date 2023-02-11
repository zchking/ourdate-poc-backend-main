# ourdate-poc-backend

This is a django backend it runs on AWS Elastic beanstalk with mysql
and on osx as a dev environment using SQL lite as the database.

With elastic beanstalk the static assets are collected and published
on a static bucket served by a cloud cdn at 
https://static.ourdate-app.com/ which gets the static assets pushed to
on every deployment.

## Deployments

Deployments to elasticbeanstalk are configured to deploy main to
the prod environment (we are deploying and testing in prod at the 
moment, at some point we will get some a staging version of the site
and app, but not for the initial POC.

The deployment pipeline is using codesuite at https://us-east-1.console.aws.amazon.com/codesuite/codepipeline/pipelines/ourdate-poc/view?region=us-east-1

## ios and android application:

The app can be found at https://www.github.com/ourdate/mvp-app

## Starting development

* `git clone git@github.com:ourdate/ourdate-poc-backend`
* If you do not have python3 installed install Python 3.x: Open your 
  terminal and type "brew install python3" to install Python 3.x on your
  Mac.
* Create a Virtual Environment: Create a virtual environment by typing 
  `python3 -m venv venvname` in the terminal.
* Activate the Virtual Environment: To activate the virtual environment,
  type `source venvname/bin/activate` in the terminal.
* `cd ourdate-poc-backend`
* Install requirements by typing `pip install -r requirements.txt`
* Setup the database: `python manage.py migrate --skip-checks`. This skip checks is important the user urls will
crash before the migrations.
* Comppile the static assets: `python manage.py collectstatic` You will need to run this a lot during development
* Start the local server with `python manage.py runserver`
* Visit the Local Server: To visit the local server, open your browser and type "localhost:8000" in the address bar

If you are testing the login flow locally run the following command:

  ```docker run --rm -it -d -p 3000:80 -p 25:25 rnwood/smtp4dev:v3```

You will be able to see the emails django sends on http://localhost:3000 

## Notes for theming

### login and password resets

We are using django-allauth for authentication you can find the base
templates at:
https://github.com/pennersr/django-allauth/tree/master/allauth/templatesr
