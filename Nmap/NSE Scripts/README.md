# Nmap - NSE Scripts

## Overview
NSE Scripts are written in `lua`. You would not want to run any `intrusive` scripts on an actual production envinronment as they will likely affect the target.

## Working with them
The `ftp-anon.nse` script can take an optional argument called `maxlist`.

## Searching for them
Searching with `grep "smb" /usr/share/nmap/scripts/script.db` can let us find the script called `smb-os-discovery.nse`. If we read into the file we can see it has a single dependency called `smb-brute`.