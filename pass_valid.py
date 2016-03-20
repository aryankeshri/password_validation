import re
pattern = "^.*(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
password = input("Enter your Password: ")
if len(password)>6:
    if len(password)<16:
        result = re.findall(pattern, password)
        if (result):
            print("Valid Password")
        else:
            print("Incorrect Password [A-Z, a-z, 1-9, @#$%^&+=]")
    else:
        print("Max Length of Password is 16 charcter")
else:
    print("min Length of Password is not between 6 Character")
