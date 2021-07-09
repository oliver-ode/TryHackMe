# Vulnversity - Compromise the webserver

## Associated files
* `phpext.txt` - List of php extensions
* `php-reverse-shell.phtml` - Reverse shell
* `nc.log` - `nc` log

## Solution
IP: `10.10.158.208`

We can semi guess that the common extension that is blocked is `.php` or we can try uploading a file and see that it is indeed blocked. Using BurpSuite we can iterate over the different extension names and find out that `.phtml` works. Renaming the end of our reverse shell to that we can then upload it and listen with `nc -lvnp 443` and then get a reverse connection to the server. After this we can simply navigate to the home directory to find the information we need with a username of `bill` and flag of `8bd7992fbe8a6ad22a63361004cfcedb`.