# The Cod Caper

## Host Enumeration

**Related files**

* `nmap.log` - Log file for `nmap` scan

All of the information required for this portion can be found by running an `nmap` scan with the `sV` and `sC` flags. The output of that can be found in the `nmap.log` file. There are `2` ports open being SSH on port 22 running version `OpenSSH 7.2p2 Ubuntu 4ubuntu2.8` and a website on port 80 running `Apache/2.4.18` with a webpage title of `Apache2 Ubuntu Default Page: It works`.

## Web Enumeration

**Related files**

* `gobuster.log` - Log file for `gobuster`

It is suggested to use `gobuster` with the `big.txt` wordlist, but I instead opted to use the `dirbuster/directory-list-2.3-medium.txt` wordlist as I had it handy. The command I used was `gobuster dir --url=http://10.10.60.59 -x html,js,php,txt --wordlist=/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50` and the log is in `gobuster.log`. The intresting file is `administrator.php`.

## Web Exploitation

**Related files**

* `sqlmap.log` - Log file for `sqlmap`

By running `sqlmap` with this command `sqlmap -u http://10.10.60.59/administrator.php --forms --dump` we can get the databse of the usernames/passwords. The output of this run is in the `sqlmap.log` file. The admin username is `pingudad` and the password is `secretpass`. By looking at the full log it seems that the webform is vulnerable to `3` types of SQLi: boolean-based blind, error-based and time-based blind.