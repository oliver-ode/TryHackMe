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

## Cracking encrypted gpg files

**Related files**
* `personal.txt.gpg`
* `data.txt`
* `data_tac.txt` - Output of `tac data.txt`
* `hash` - John readable format of `personal.txt.gpg`
* `personal.txt` - Final decrpted version of `personal.txt.gpg`

### Copying files across

GPG: `scp /home/sarah/oldLogs/units/personal.txt.gpg .`

Wordlist: `scp /home/sarah/logs/zmn/old\\\ stuff/-mvLp/data.txt .`

Tac'n the wordlist `tac data.txt > data_tac.txt`

### John

`gpg2john personal.txt.gpg > hash`

Using `john --wordlist=data_tac.txt --format=gpg hash` we get a password of `valamanezivonia`. We can then run `gpg personal.txt.gpg` and get an output file of `personal.txt` which contains the solution.

## Reading SQL databases

We can find the database to be located at: `/home/sarah/serverLx/employees.sql`. We can get into a `mysql` command prompt and run `USE employees` and then `DESCRIBE employees`. We can check `first_name` and `last_name` for the flag by running the following command (changing the field): `SELECT * FROM employees WHERE last_name LIKE '%{%}';`. Running this will show one entry which is our flag `Flag{13490AB8}`.

## Final Challenge

### Initial instructions

Located in the file `/home/shared/chatlogs/LpnQ` is:

```
(2020-08-13) Sarah: Hey Lucy, what happened to the database server? It is completely down now!

(2020-08-13) Lucy: Yes, I believe we have had a problem. I will need to investigate but for now there will be downtime for who knows how long.

(2020-08-13) Sarah: That is a shame, I needed to refer to a customer’s record due to them being unhappy with our service yesterday.

(2020-08-13) Lucy: if you ask Sameer, he may be able to help you find the back-up database copy we made a few hours ago?

(2020-08-13) Sarah: Of course, he is one of the sql developers around here in charge of the database creation, I will ask him in a few minutes. Thank you.

(2020-08-13) Lucy: No problem. By the way, our new security engineer may have accidently stored the SSH password of one of our employees. I have no idea how to change it and he will not be back till tomorrow.

(2020-08-13) Sarah: That is a shame. I am sure we will all be fine till he returns. Do you know which employee it is?

(2020-08-13) Lucy: I think it may have affected James but I not entirely sure.

(2020-08-13) Sarah: That is terrible, but I am sure nothing will come of it, he will be back tomorrow.

(2020-08-13) Lucy: True. It is just a concern of mine because James is the only one with root access. But as you said, we should be ok. Talk to you later. Bye.
```

### SSH password and location of back-up

Using `grep back-up *` we can search for all files that contain the word "back-up" which is 2 new file apart from `LpnQ` which are `Pqmr` and `KfnP`.

Contents of `Pqmr`
```
(2020-08-13) Sarah: Hey Sameer, do you by any chance no where I can find the sql back-up copy on this system? The database server is down, and I really need to help a customer out.

(2020-08-13) Sameer: Sure. let me check.

(2020-08-13) Sarah: Thanks.

(2020-08-13) Sameer: check the home/shared/sql/ directory. It should be in there with the date of today.

(2020-08-13) Sarah: Thank you Sameer.

(2020-08-13) Sameer: No problem. It probably is encrypted. Just use the password: danepon.

(2020-08-13) Sarah: OK, thank you.

(2020-08-13) Sameer: No problem

(2020-08-13) Sameer: By the way, if you have any issues just talk to Michael as I will be off for the remainder of the day. See you tomorrow. Bye.

(2020-08-13) Sarah: Bye.
```

Contents of `KfnP`
```
(2020-08-13) Sarah: Michael, I have been having trouble accessing the sql database back-up copy made today. Sameer gave me the password, but it just will not work?

(2020-08-13) Michael: Ah, yes. I remember, the security engineer was testing out a new automated software for creating sql database backups. He must have configured it to encrypt the backups with a different password.

(2020-08-13) Sarah: So how can I get a hold of it?

(2020-08-13) Michael: Good question. From what I remember the test program utilised a configuration file around 50mb. It is located inside the home/shared/sql/conf directory. This configuration file contained the directory location of a wordlist it used to randomly select a password from for encrypting the sql back-up copies with. 

(2020-08-13) Sarah: I do not really understand the last part?

(2020-08-13) Michael: once you find the configuration file and consequently the wordlist directory, visit it. One of those wordlists must contain the password it used for the testing. All I remember is that the password began with ebq. You will need Sameer’s account. His SSH password is: thegreatestpasswordever000. 

(2020-08-13) Sarah: Thank you, I will try to find it.
```

From these messages we know the following:
* `James` has a leaked password and has root access
* `/home/shared/sql/` is the location of the encrypted back-up database
* `/home/shared/sql/conf/` contains a `50mb` file that has the wordlist location for the actual password
* The password in the wordlist begins with `ebq`
* Sameer's SSH password is `thegreatestpasswordever000`

### Back-up database password

Using `find /home/shared/sql/conf * -type f -size 50M` we can search for all files that are 50mb and it will only return a single file called `JKpN`. Looking in the file it has a header that contains the location of the wordlist at `aG9tZS9zYW1lZXIvSGlzdG9yeSBMQi9sYWJtaW5kL2xhdGVzdEJ1aWxkL2NvbmZpZ0JEQgo=`. This seems to be base64 so we can use `echo "aG9tZS9zYW1lZXIvSGlzdG9yeSBMQi9sYWJtaW5kL2xhdGVzdEJ1aWxkL2NvbmZpZ0JEQgo=" | base64 -d` to get the actual location of `home/sameer/History LB/labmind/latestBuild/configBDB`. Inside of that directory we can use `cat * | grep "ebq"` to get a list of all strings that start with `ebq` which is:

```
ebqiuiud
ebqjoisjdfij
ebqiojsdfioj
ebqiojsiodj
ebqiojdifoj
ebqiopsjdfopj
ebqnice
ebqops
ebqkjjdd
ebqijsji
ebqopkopk
ebqattle
```

We can manually brute force through all of these to find out that the password is `ebqattle`.

### Finding James's password and getting the flag.

With the encryption key we can decrypt the `.gpg` and then unzip it. There are a bunch of `.dump` files which seem to contain potentially relevant information. We can search for James in the files by running `grep -rn *.dump -ie "james"` which returns one entry that contains the string `vuimaxcullings` which is James's password! We can ssh into his account and since he has root access we can run `sudo bash` to get a terminal as root and then simply navigate to `/root` and `cat` out the flag: `Flag{6$8$hyJSJ3KDJ3881}`