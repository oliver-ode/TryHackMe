# Linux Strength Training

## Finding your way around linux - overview

### What is the correct option for finding files based on group:
`-group`

### What is format for finding a file with the user named Francis and with a size of 52 kilobytes in the directory /home/francis/
`find /home/francis -type f -user Francis -size 52k`

### Initial SSH prompt

File is: `2019-10-11`

Characters subsequent are: `ttitor`

### Flag Search

Initial file is located at: `/home/topson/ReadMeIfStuck.txt` and contains:
```
Looking for flag 1?:It seems you will have to think harder if you want to find the flag. Perhaps try looking for a file called additionalHINT if you can't find it..
Looking for flag 2?: look for a file named readME_hint.txt
```
The file `additionalHINT` can be found using `find / * | grep additionalHINT` and is located at `/home/topson/channels/additionalHINT`. The text that it contains is:
```
try to find a directory called telephone numbers... Oh wait.. it  contains a space.. I wonder how we can find that....
```
We can search for the directory using `find / -type d -name "telephone numbers"` and see that it is located at `/home/topson/corperateFiles/xch/telephone numbers`. The text file in the directory contains:
```
202-555-0150
202-555-0125
617-555-0115
+1-617-555-0115 
+1-617-555-0186
+1-617-555-0138
use the Find command to find a file with a modified date of 2016-09-12 from the /workflows directory
```
Using the command: `find / -type f -newermt 2016-09-11 ! -newermt 2016-09-13` we find the file `workflows/xft/eBQRhHvx`. Looking through this file we can search for a `{` and find the flag of: `Flag{81726350827fe53g}`.

## Working with files

### Move all files in current directory to /home/francis/logs
`mv * /home/francis/logs`

### SCP file transfer
`scp /home/james/Desktop/script.py john@192.168.10.5:/home/john/scripts`

### Rename folder from -logs to -newlogs
`mv -- -logs -newlogs`

### Copy file named encryption keys to the directory of /home/john/logs
`cp encryption\ keys /home/john/logs`

### Flag search

From the file looked at before we need to search for a file called `readME_hint.txt` with `find / * | grep readME_hint.txt` to find that it is located at `/home/topson/corperateFiles/RecordsFinances/readME_hint.txt` and contains the text:
```
Instructions: Move the MoveMe.txt file to the march folder directory and then execute the SH program to reveal the second flag.

 you need to research three things:
                                 how to execute bash files
                                 how to work with files that begin with a - (dash) whether that is to do with copying or moving files 
                                 how to work with files with spaces
```
To move the file we can navigate to the `RecordsFinances` directory and execute `mv -- -MoveMe.txt -march\ folder`. Then we can simply run `./-runME.sh` to get the flag of `Flag{234@i4s87u5hbn$3}`.

## Hashing - introduction

**Related files**
* `hash1.txt`
* `hashA.txt`
* `hashB.txt`
* `hashC.txt`
* `ww.mnf`

### hash1.txt

Running `john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash1.txt` gives us a password of `secret123`

### hashA.txt

Using `hash-identifier` we can see that the hash is an `MD4` hash. We can look that up [here](http://pentestmonkey.net/cheat-sheet/john-the-ripper-hash-formats) to find a format of `raw-md4`. Using `john --format=raw-md4 --wordlist=/usr/share/wordlists/rockyou.txt hashA.txt` will then give us a password of `admin`.

### hashB.txt

Using `hash-identifier` we can see that the has is an `SHA-1` hash. Looking up in the previous website we can find the format of `raw-sha1`. Using `john --format=raw-sha1 --wordlist=/usr/share/wordlists/rockyou.txt hashB.txt` will then gives us a password of `letmein`

### hashC.txt

We can copy the wordlist over to our local system using `scp` and then we can use `hash-identifier` to see that it is a `SHA-256` hash. The website gives us a format of `raw-sha256` which we can use in the command `john --format=raw-sha256 --wordlist=ww.mnf hashC.txt` to get a password of `unacvaolipatnuggi`.

## Base64

**Related files**
* `hashSpecial.txt` - Hash from `ent.txt`

### Tool

The tool is the one that is mentioned above: `base64`.

### encoded.txt

Piping the text file `encoded.txt` into `base64` gives us a large block of text that tells us to search for the string `special`. Searching for this leads us to the file `ent.txt`. This seems to be in a hash so we can run `hash-identifier` to see that it is in fact a `MD5` hash. Using `john` with the `rockyou.txt` wordlist will give us a password of `john` which is the special answer.

## Encryption/decryption w/ gpg

### Flag

`gpg /home/sarah/system\ AB/keys/vnmA/layer4.txt` (password = `bob`) gives us a hint to find `layer3.txt`

`gpg /home/sarah/oldLogs/2014-02-15/layer3.txt` (password = `james`) gives us a hint to find `layer2.txt`

`gpg /home/sarah/oldLogs/settings/layer2.txt` (password = `tony`) gives us the string of `MS4gRmluZCBhIGZpbGUgY2FsbGVkIGxheWVyMS50eHQsIGl0cyBwYXNzd29yZCBpcyBoYWNrZWQu`

The string seems to be a base64 string so we can use `echo "MS4gRmluZCBhIGZpbGUgY2FsbGVkIGxheWVyMS50eHQsIGl0cyBwYXNzd29yZCBpcyBoYWNrZWQu" | base64 -d` which gives us a hint to find `layer1.txt`

`gpg /home/sarah/logs/zmn/layer1.txt` (password = `hacked`) which gives us the final flag `Flag{B07$f854f5ghg4s37}`
