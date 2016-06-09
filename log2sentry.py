#!/usr/bin/env python
__author__ = 'Mahmoud Adel <mahmoud.adel2@gmail.com>'


import argparse
from raven import Client as SentryClient


dsn = ''  # Your Sentry DSN here
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--application', dest='app', metavar='APP_NAME', help='Application name, e.g. Nginx, MySQL', required=True)
parser.add_argument('-l', '--log-file', dest='logfile', metavar='LOG_FILE', help='Log file to monitor', required=True)
args = vars(parser.parse_args())
app = args['app']
logfile = args['logfile']


def tellsentry(message):
    client = SentryClient(dsn)
    client.captureMessage(message, Tags={'app': app})


def watchlog(logfile):
    with open(logfile) as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                message = '''%s: %s
Message from: %s
                ''' % (app, line, logfile)
                tellsentry(message)


def main():
    try:
        watchlog(logfile)
    except IOError:
        print '%s not found!' % logfile
        exit(1)
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()
