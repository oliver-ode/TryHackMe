# Advent of Cyber 2 - Day 23

## Steps

### Fake Bitcoin Address
The bitcoin address in the note is `bm9tb3JlYmVzdGZlc3RpdmFsY29tcGFueQ==` and we can see that it is encoded in base 64. Using an online converter we get a plain text of `nomorebestfestivalcompany`.

### Tasks
When looking at the Documents folder we see that the files have an extension of `.grinch`. The name of the suspicious task that is running is `opidsfsdf`. The actual `.exe` that it runs is loacated at: `C:\Users\Administrator\Desktop\opidsfsdf.exe`. The ShadowCopyVolume ID is `7a9eea15-0000-0000-0000-010000000000`.

### Partition
The name of the hidden folder once the partition is mounted is `confidential`. Once we restore the old version of the folder we can open the master password text file and get the password of `m33pa55w0rdIZseecure!`.