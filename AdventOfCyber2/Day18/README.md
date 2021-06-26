# Advent of Cyber - Day 18

## Steps

### General steps
We can deploy the AttackBox and then connect to the server. If we run ILSpy on on the .exe we can decompile the code. If we go into the `CrackMe` section we can see a `MainForm` section and a function called `buttonActivate_Click`. We can see there are two output texts at the bottom and the valid one contains the flag `thm{046af}`. For the password we can see at the top there is a variable `ptr` that gets it's value from a weird string. We can see `santapassword321` inside of it which is correct as the password, but to check we can also double click on it and see a hexadecimal representation of it which we can verify to be the same.