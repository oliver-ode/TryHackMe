# Advent of Cyber 2 - Day 1

## Steps

IP: `10.10.38.82`

### Cookie information

My account registration username was `asdf` and the password was `12345` to just keep it simple.

The login cookie is called auth and my specific cookie has a value of `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2261736466227d`

By looking at the key we can see that it uses number 0-9 and letters a-f which is 16 different characters. This means that we are in hexadecimal. We can use an online convertor to convert the login cookie to `{"company":"The Best Festival Company", "username":"asdf"}`. This format is JSON.

### Bypassing cookie authentication

We can simply take the JSON format and change the username to be "santa" and convert this over to hexadecimal. Doing this gives us a cookie value of `7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d`. We can create a new cookie with name `auth` and a value of the above and we can login as santa! After this we can tick all sliders and get the flag of `THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}`