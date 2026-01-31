reg_no="AP24110011607"
last_digit=int(reg_no[-1])
Student=input("Enter Student ID: ")
digit_found=False
student_valid=False
if len(Student) == 7:
    if Student[4].isdigit() and Student[5].isdigit() and Student[6].isdigit():
        digit_found = True
    if Student[0]=="C" and Student[1]=="S" and Student[2]=="E" and Student[3]=="-" and digit_found:
        student_valid = True
Email=input("Enter Email Id: ")
valid_Email=False
valid_end=False
if Email[-4:] == ".edu":
    valid_end = True
if '@' in Email and '.' in Email and Email[0]!='@' and Email[-1]!='@' and valid_end:
    valid_Email=True
password=input("Enter Password: ")
valid_password=False
if len(password) >= 8:
    if password[0]>= 'A' and password[0]<= 'Z':
        if any(ch.isdigit() for ch in password):
            valid_password = True
Referral=input("Enter Referral: ")
valid_Referral=False
valid_start=False
if len(Referral) >= 6:
    if Referral[0]=="R" and Referral[1]=="E" and Referral[2]=="F":
        valid_start = True
    if valid_start and Referral[3].isdigit() and Referral[4].isdigit() and Referral[-1]=="@":
        valid_Referral = True
if last_digit%2 !=0:
    approved=valid_password and student_valid
else:
    approved=student_valid and valid_password
if approved and valid_Email and valid_Referral:
    print("Approved")
else:
    print("Rejected")



