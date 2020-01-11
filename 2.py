import re

un=input("Username= ")
pw=input("Password= ")
x=re.search("\A[a-z]",un)
y=re.search("(?=.*\w\d){4,11}$",un)
if (x)and(y):
        print("True")
else:
    print("False")
if re.search("^([\d]{1})([A-Z]{5})([#?!@$%^&*-+=_`~]{1})[\w\d#?!@$%^&*-+=_`~]{,7}$",pw):
    print("True")
else:
    print("False")
