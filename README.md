**log2sentry:**

Monitor log files and send messages to Sentry.

**Installation:**

`sudo wget https://raw.githubusercontent.com/mahmoudadel2/log2sentry/master/log2sentry -O /usr/local/bin/log2sentry`

`sudo chmod u+x /usr/local/bin/log2sentry`

**Usage examples:**

`log2sentry -a AppName -l /path/to/logfile`

`log2sentry -a Nginx -l /var/log/nginx/error.log`


**Uninstallation:**

`sudo rm -v /usr/local/bin/log2sentry`
