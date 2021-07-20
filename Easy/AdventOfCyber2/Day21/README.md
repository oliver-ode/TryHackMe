# Advent of Cyber 2 - Day 21

## Steps

### Hashes
We can view the hash of the text file in Documents and see that it is `596690FFC54AB6101932856E6A78E3A1`. When we get the hash of the actual `.exe` file we get a MD5 hash of `5F037501FB542AD2D9B06EB12AED09F0` which is evidently different.

### Streams
If we use `strings` we can find the hidden flag of `THM{f6187e6cbeb1214139ef313e108cb6f9}` inside of the `.exe`. When we look at the streams associated with the `.exe` we see that there is a stream called `hidedb`. We are then able to run the `.exe` with that stream and get the flag of `THM{088731ddc7b9fdeccaed982b07c297c}`.