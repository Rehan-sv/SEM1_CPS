login_attempts = [" alice ", " bob", " eve", " alice ", " mallory ", " frank ", " eve"]
authorized_users = {" alice ", "bob ", " frank ", " grace "}
b=set(login_attempts)
x=b-authorized_users
print(x)