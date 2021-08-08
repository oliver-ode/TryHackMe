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