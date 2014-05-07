gae-url-pinger
==============

This app is intended to run on google app engine. It sends requests to specified 
urls in scheduled intervals.  
Purpose of this app is to keep alive web applications in hosted and cloud 
environments that can be put in suspended state after longer idle period 
(for example [OpenShift](https://www.openshift.com/)).

You can use this app directly from github by forking it to your github account 
and using [push to deploy](https://developers.google.com/appengine/docs/push-to-deploy) 
functionality of google app engine.

HTTP responses to requests are logged into app engine logs, so you can check 
if everything is allright. For example you can check if your urls are still alive 
for specified ping period.


## Configuration

### List of URLs

You can specify list of urls in `pinger.py` file by editing `urls` variable.


### Ping time interval

You can specify how often should this app send request to urls by editing `cron.yaml` file.


## References

- inspired by [google-pinger](https://github.com/figurebelow/google-pinger)
