# Advent of Cyber 2 - Day 6

## Steps

IP: `10.10.136.178`

### Questions
By looking at the length of the first prompt we can guess that is is `stored cross-site scripting`. By searching in the database we can find out that `q` is the query string. By running `OWASP ZAP` we can scan the website and see that it multiple results. In my case I had to guess as the number I was given was different, but the solution is `2`. To get an alert showing we can input `</p><script>alert(1);</script<p>`.