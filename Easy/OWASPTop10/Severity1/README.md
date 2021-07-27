# OWASP Top 10 - Severity 1

## Strange file
CMD: `ls`
ANS: ``

## Number of regular users
CMD: `compgen -u | wc -l`
ANS: `0`

## Current user
CMD: `whoami`
ANS: `www-data`

## Current users shell
CMD: `getent passwd | cut -d: -f1,7`
ANS: `/usr/sbin/nologin`

## Version of Ubuntu
CMD: `lsb_release -a`
ANS: `18.04.4`

## MOTD
CMD: `cat /etc/update-motd.d/00-header`
ANS: `DR PEPPER`