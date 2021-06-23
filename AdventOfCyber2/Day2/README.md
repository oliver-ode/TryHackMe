# Advent of Cyber 2 - Day 2

## Associated files
* `php-reverse-shell.php` - Default PHP reverse shell script found on Kali modified for this problem

## Steps

IP: `10.10.113.55`
ID Number: `ODIzODI5MTNiYmYw`

### Configuring reverse shell script
Need to change port to `443` and the VPN IP associated with my system is `10.6.85.73`. When we look at the website which we can access via `10.10.113.55?id=ODIzODI5MTNiYmYw` we can see that the upload accepts images which means we will append `.jpeg` to our script so we can upload it.

### Finding directory
It is possible to guess that it is at `uploads`, but I instead decided to just run `DirBuster` with wordlist `directory-list-2.3-small.txt` which showed `uploads` is available on the server.

### Getting reverse connection and flag
Once you have everything set up run `sudo nc -lvnp 443` and load the file on the server. You should then have a reverse connection and be able to navigate on the server to get a flag of `THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}`.