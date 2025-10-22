import re 
blesss=re.compile(r'')
while True:
    password = input("Enter your password: ")
    if (len(password)<4):
        print("Password must be at least 4 characters long.")
    elif re.search(r'\d', password) is None:
        print("Password must contain digits.")
    elif re.search(r'\w', password) is None:
        print("Password must contain letters.")
    elif re.search(r'\s',password) is not None:
        print("Password must not contain spaces.")
    elif re.match(r'^[a-zA-Z0-9_]+$', password) :
        print("ur pass is valid")
        break
    else:
        print("YEHEEEEEE Gotcha.")