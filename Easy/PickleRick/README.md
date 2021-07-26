# Pickle Rick

## First ingredient

### Nmap
Ubuntu System
Open ports:
* `22` - SSH
* `80` - Apache

### Default Apache page
There is a comment in the HTML saying that the username is `R1ckRul3s`.

### Dirbuster
Login portal at `login.php` and `portal.php`. We also see that the website contains a `robots.txt` file that has the text `Wubbalubbadubdub`. This is actually the password for the login portal.

### Portal
We get access to a very basic shell and if we `ls` the default directory we can see a file called `Sup3rS3cretPickl3Ingred.txt`. Since this is in the website directory we can simply open it up and get the first ingredient.

### Ingredient
`mr. meeseek hair`

## Second ingredient

### Reverse Shell
We can use a Python 3 reverse shell to get better access to the server. Once we get access to the shell we can check out the `home` directory and find a `rick` user. If we go navigate in here we can find a text file called `second ingredients` and simply `cat` it out to get the second ingredient.

### Ingredient
`1 jerry tear`

## Third ingredient

### Stabilize shell
To make it easier on ourselves we can stabilize the shell using a Python method to have autocomplete and an overall improved experience.

### Linpeas
We can copy `linpeas` over to the server by making a python `SimpleHTTPServer` on our local machine and download and run the script over on the remote machine. After running it we can see that the user `www-data` we can see that with `sudo` we can run all commands without any password: `(ALL) NOPASSWD: ALL`. This just allows us to run `sudo bash` to get a new terminal with rull root access. After this we can just simply navigate to `/root` and `cat` out the `3rd.txt` file to get the final ingredient.

### Ingredient
`fleeb juice`