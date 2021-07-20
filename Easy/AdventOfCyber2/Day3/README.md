# Advent of Cyber 2 - Day 3

## Steps

IP: `10.10.173.128`

### Attacking the login form
Using `BurpSuite` we can analyze a packet that is being sent when logging in and then automate the process of spamming the server. By doing that we can see that the login combination is `admin` as the username and `12345` as the password.