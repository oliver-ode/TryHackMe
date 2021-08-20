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

## Command Execution

With the web shell we have access to run some basic commands. We can firstly run `ls` in our directory to find see that there are `3` files located in the directory. For finding if Pingu still has an account we can look at the `/etc/passwd` file to see that indeed he still has an account. To check for his password we can use `find / -name *pass* -type f 2> /dev/null` to find all files that have the string "pass" inside of them. There is a file called `/var/hidden/pass` which seems interesting and if we `cat` out the contents we can see that his SSH password `pinguapingu` is located in there.

## LinEnum

Since we are searching for a SUID file we could use linpeas, but that is a bit overkill. Instead using `find / -perm -4000 2>/dev/null` is faster and it reveals a file called `/opt/secret/root` which has the SUID bit set.

## Finishing the job

Now that we have a hash we can try to crack it. Looking on [this](https://hashcat.net/wiki/doku.php?id=example_hashes) it seems that hashcat treats this hash as ID `1800`. Running hashcat with `hashcat -a 0 -m 1800 hash /usr/share/wordlists/rockyou.txt` will now give us the password which is `love2fish`.