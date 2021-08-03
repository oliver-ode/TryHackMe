# Root Me
IP: `10.10.16.212`

**Related files**
* `nmap.log` - Nmap output
* `php-reverse-shell.phtml` - Reverse shell script

## Reconnaissance
Running an `nmap` scan on the IP gives us 2 ports being `ssh (22)` and `apache (80)`. The Apache instance is running version `2.4.29`. Running `DirBuster` on the website returns a hidden direcotry of `/panel`.

## Getting a shell
Looking at the panel directory we can see that it is a file upload page. Attempting to upload the standard `php-reverse-shell.php` file results in an error as the `.php` extension is blocked. Changing it to `.phtml` bypasses the filter and then navigating to the `/uploads` page allows us to find and run the script while having `nc -lvnp 443` running. Once in we can run `find * | grep user.txt` to find the location of the `user.txt` file which is in the `/var/www` directory. It contains the flag `THM{y0u_g0t_a_sh3ll}`.

## Privilege escalation
To find which binaries have SUID permissions set we can run `find / -perm -4000 2>/dev/null`. Looking through the output the `/usr/bin/python` binary seems out of place. Looking at SUID and python on GTFOBins gives the following command that will gives us a shell with root privilege `/usr/bin/python -c 'import os; os.execl("/bin/sh", "sh", "-p")'`. After this we can simply `cat` out the root flag: `THM{pr1v1l3g3_3sc4l4t10n}`.