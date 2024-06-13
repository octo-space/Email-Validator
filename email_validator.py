import re

regex = r"^[a-zA-Z0-9._]+@[a-zA-z0-9]+\.[a-z]{2,}$"

em = input(" enter your mail: ")

if re.match(regex, em):
    print(" VALID E-MAIL")
else:
    print("NOT VALID E-MAIL")
 
