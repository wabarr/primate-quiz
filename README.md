primate-quiz
============

## New (to me) django techniques in this project

* Use [django-mobile] (https://github.com/gregmuellegger/django-mobile) middleware to serve mobile version of content
* simple tweak to views.py to toggle variable 'useGoogleAnalytics' based on current user permissions.  Use this variable in template to prevent tracking admin visits to the site
* implement facebook share button.  Doesn't work exactly as I want it, because the image that gets shared on facebook turns out to be the banner image from the front page. This must have to do with the open-graph tags, but I haven't taken the time to figure it out.
* serve amazon.com ads
