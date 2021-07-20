# Advent of Cyber 2 - Day 4

## Associated files
* `wordlist` - Provided date wordlist

## Steps

IP: `http://10.10.230.227/`

### Format for fuzzing Shibes
We can use the example command that they gave and modify it to work for the required purpose: `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ`

### Finding the directory
Using `Gobuster` with the following command we can search for all directories on the server: `gobuster dir -u http://10.10.230.227 -w /usr/share/wordlists/dirb/big.txt`

### Fuzzing the file for the date
We can use `wfuzz` by modifying the example command to be `wfuzz -c -z file,wordlist http://10.10.230.227/api/site-log.php?date=FUZZ` to find out the correct date information is `20201125`. After this we get the flag to be `THM{D4t3_AP1}`.