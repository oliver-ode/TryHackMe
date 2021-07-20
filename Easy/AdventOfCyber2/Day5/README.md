# Advent of Cyber 2 - Day 5

## Associated files
* `burp_out` - Saved `BurpSuite` command
* `sqlmap.out` - Output of `sqlmap`

## Steps

IP: `10.10.145.52`

### Bypassing login panel
The secret panel is located at `santapanel` and we can use SQLi to get in. By settings the username to `asdf' or 1==1 --` and the password to anything it will log us in.

### Getting all of the SQL information
We can use `sqlmap` to get an output of the SQL table. First, record a table request using `BurpSuite` and save it in a file. Then using the following command we can get the database information `sqlmap -r burp_out --tamper=space2comment --dump-all --dbms sqlite | tee sqlmap.out`. After this we can simply read the information and see that there are `22` entires, Paul wants `github ownership`, the flag is `thmfox{All_I_Want_for_Christmas_Is_You}` and the `admin` password is `EhCNSWzzFP6sc7gB`.