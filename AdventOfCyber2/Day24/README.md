# Advent of Cyber 2 - Day 24

## Associated files
* `nmap.log` - Initial `nmap` scan
* `php-reverse-shell.jpeg.php` - `php` reverse shell script that we uploaded
* `reverse_connection.log` - `tmux` log for the reverse connection portion

## Steps
IP: `10.10.221.146`

### Nmap scan
When scanning the machine with `nmap` we can see that ports `80` and `65000` are open. Port `65000` has a title of `Light Cycle`.

### Website stuff
I used a mix of `dirbuster` and `gobuster` to find the hidden page and directory. Using `dirbuster` I found the hidden php page called `uploads.php` and using `gobuster` I found the hidden directory `grid`. Both of them were run using `directory-list-2.3-small.txt` from `dirbuster`. We can take the simple reverse shell script and change the IP to our IP and the port to `443` and then upload it to the upload page. To bypass the client side filter we can use BurpSuite to drop the verification JavaScript file and to bypass the server filter we can rename the script to fool the server into thinking it is an image. Once we have uploaded it can we listen with `nc -lvnp 443` and execute the script.

### Reverse connection
I used `find -name 'web.txt'` to find the file and I saw that it was located in `/var/www/web.txt` the flag was `THM{ENTER_THE_GRID}`. At this stage it makes sense to upgrade the shell to make it easier on us to actually perform the rest of this challenge. We can go into `TheGrid/includes` and see a file called `dbauth.php`. Inside of this file we get a username and password combination for a MySQL database. The username is `tron` and the password is `IFightForTheUsers`.

### Database
We can login to the database using this information and see that there is a database called `tron` and inside a table called `users`. If we list this we can see a credential details for a user called `flynn` with an encrypted password of `edc621628f6d19a13a00fd683f5e3ff7`. We can put this onto an online cracking site such as `crackstation` and see that the decrypted password is `@computer@`. Using this we can login to the `flynn` user.

### Final flags
Once we login to the user we can simply `cat` the value of `user.txt` and get the flag of `THM{IDENTITY_DISC_RECOGNISED}`. If we list the groups that `flynn` is associated with we can see a `lxd` group. We can abuse this to get the final flag hidden behind root privileges. We can list the ldc containers using `lxc image list` and see that there is an Alpine image already installed. We can set it up and mount the entire drive using `lxc config device add alp dsk disk source=/ path=/mnt/root` where `alp` is the name of the contianer and `dsk` is the name given for the drive. Once it is set up we can run it and start a shell. Once in we can simply navigate into the directory and `cat` out `root.txt` and get a value of `THM{FLYNN_LIVES}` along with a nice leaving message!