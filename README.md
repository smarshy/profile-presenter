# profile-presenter

## Dependencies required:

Django version 1.8 (tested) and above

Feel free to point out if versions go wrong

## Get it up and running

1. Clone the project
2. You will need a Github access token. Get it following [this](https://github.com/blog/1509-personal-api-tokens). Please replace your own token in git_api_interactions.py. (This is necessary)
3. cd into the directory, migrate and runserver

Also, If you are running into insecure platform warnings, see [this](http://stackoverflow.com/questions/29134512/insecureplatformwarning-a-true-sslcontext-object-is-not-available-this-prevent) 

## What does this do?

I wrote this over the weekend to have fun with my github data. It pulls data from Github API, performs a bit of statistical analysis on it and renders it using Google Charts. 

Currently, it shows you different charts (column/pie/area) for

1. Pull request and Issue count
2. Commit frequency for the last month in terms of days in the week
3. Pull request statuses
4. Programming language analysis for your repositories

To see a version of what it should look like, I have pushed up my profile [here](http://profilepresenter.herokuapp.com/)

P.S. There are a few existing problems I ran into. Still need to be fixed. Find them [here](https://github.com/smarshy/profile-presenter/issues)
