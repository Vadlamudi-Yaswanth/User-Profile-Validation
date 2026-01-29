Name=input("Enter Your Name:")
valid_name=False
if len(Name.split())>=2 and Name[0]!=" "  and Name[-1]!=" ":
    valid_name=True
Email_Id=input("Enter Your Email Id:")
valid_email=False
if Email_Id[0]!='@':
    if '.' in Email_Id and '@' in Email_Id:
        valid_email=True
    else:
        valid_email=False
Number=input("Enter Your Number:")
valid_number=False
if len(Number)==10 and Number.isdigit() and Number[0]!='0':
    valid_number=True
Age=int(input("Enter Your Age:"))
valid_age=False
if Age>=18 and Age<=60:
    valid_age=True
if valid_name and valid_email and valid_number and valid_age:
    print("User Profile is Valid")
else:
    print("User Profile is Invalid")