# Kenobi

## Related Files
* `deploy.log` - `tmux` log for deploy section
* `enumerate.log` - `tmux` log for enumerate section
* `ProFtpd.log` - `tmux` log for FTP section
* `id_rsa` - RSA private key for `ssh` purposes
* `PrivEsc.log` - `tmux` log for privilege escalation section

## Deploying
* `7` ports are open

## Enumerating Samba Shares
* `3` shares are open
* `log.txt` is available in the anonymous share
* `21` is the port FTP is running on
* `/var` is a mount available on the system

## ProFtpd
* `1.3.5` is the version of ProFtpd the server is running
* `3` exploits are visibile
* `d0b0f3f53b6caa532a83915e19224899` is the flag at `/home/kenobi/user.txt`

## Privilege Escalation
* `/usr/bin/menu` looks interesting
* `3` options are available from the binary
* `177b3cd8562289f37382721c28381f02` is the flag at `/root/root.txt`