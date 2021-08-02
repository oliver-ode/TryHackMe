# Simple CTF
IP: `10.10.2.248`

**Related files**
* `nmap.log` - Nmap output
* `exploit.py` - Exploit script for `CVE-2019-9053`
* `exploit.log` - `CVE-2019-9053` script output

## Initial look
Initially I did an nmap scan scan to get some info on ports for the first two questions and to get an idea of what is running. The output of the scan is located at `nmap.log` and via it we can see 2 services on ports < 1000 and that SSH is running on the higest port.

## Dirbuster
We can go on the webpage and look around and see that it is a default Apache install on Ubuntu. To get some more info, running dirbuster with the `directory-list-2.3-medium.txt` wordlist we can eventually find a `simple` directory. This a `CMS Made Simple` instance. 

## Exploit
Looking up on Exploit-DB we can find that the specific version running is vulnerable to `CVE-2019-9053` which is an SQL Injection (SQLi) based vulnerability. Downloading the script we need to convert it over to Python 3 with the 2to3 module and change line 56 to include an encoding format. After running this we can find the password of `secret`.

## Next step
After looking at the admin panel in the web page for a bit I could not find anything that would help move forwards. I decided to give the credentials a try in the SSH hosted on port `2222` and it worked! Once in we can see the user flag of `G00d j0b, keep up!` in the home folder of `mitch` and another user called `sunbath`.

## Getting root
I copied `linpeash` over with SCP and ran it and saw that `mitch` could run `vim` with no password using `sudo`. We can search up `vim` and `sudo` on GTFOBins and find the following exploit `sudo vim -c ':!/bin/sh'`. Using this we can spawn a privileged terminal with full root permissions. After this we can simply move to the root directory and `cat` out the final flagL `W3ll d0n3. You made it!`.