# Advent of Cyber 2 - Day 14

## Associated files
* `fullres.jpeg` - Downloaded image from Twitter

## Steps

### Reddit associated steps
We can search up his username on reddit and find out that he was born in Chicago. If we search up Robert who was his creator and Rudolf we get Robert L. May as the creator of Rudolf.

### Twitter associated steps
If we search up the username we can see a Twitter account. His favourite show was "Bachelorette" and the Christmas parade that he was at was in Chicago. If we download the fullres photo hosted on the website, we can get the EXIF information for the location of `41.891815, 87.624277` and the flag of `{FLAG}ALWAYSCHECKTHEEXIFD4T4` for the copyright information.

### Other
If we use have `haveibeenpwned` we can see that was was in a password breach. We can then use `scylla.sh` to search for his email to get his password of `spygame`. When we look up the hotels in the area mentioned, we can eventually find the Chicago Marriott hotel which has an address of `540 North Michigan Ave`.