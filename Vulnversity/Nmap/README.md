# Vulnversity - Reconnaissance

## Related files
* `tmux.log` - `tmux` log file

## Solutions
IP: `10.10.138.73`

When scanning the machine we can see that there are `6` open ports and the Squid proxy is running version `3.5.12`. If the `-p-400` flag were to be used it would only scan `400` ports. The flag `-n` does not resolve DNS as seen in the `man` page `-n/-R: Never do DNS resolution/Always resolve [default: sometimes]`. Looking at the Apache server we can gguess that the server is most likely running `Ubuntu` as the OS. The web server in this case is an Apache server running on port `3333`.