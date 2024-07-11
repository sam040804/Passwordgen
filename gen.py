import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz:;+!@#$%^&*(){[]}"
length_password = int(input("enter password length:"))
a = "".join(random.sample(password,length_password))
print(f"Password is {a}")