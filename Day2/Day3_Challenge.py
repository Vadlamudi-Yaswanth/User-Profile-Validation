n=int(input("Enter the no.of students marks to be entered:"))
marks=[0]*n
for i in range(n):
    marks[i]=int(input(f"Enter the mark of  student {i+1}:"))
reg_no=input("Enter the registration number:")
name=input("Enter your name:")
section=input("Enter the section:")
count1=0
count2=0
if reg_no[-1]=="2" or reg_no[-1]=="3" or reg_no[-1]=="5" or reg_no[-1]=="7" or reg_no[-1]=="9":
    for i in range(len(marks)):
        marks[i]+=5
else:
    for i in range(len(marks)):
        marks[i]+=2
if len(name)>=8:
    for i in range(len(marks)):
        marks[i]+=8
else:
    for i in range(len(marks)):
        marks[i]+=6
if section=="A" or section=="E" or section=="I" or section=="O" or section=="U":
    for i in range(len(marks)):
        marks[i]+=5
else:
    for i in range(len(marks)):
        marks[i]+=2
print(marks)
for mark in marks:
    if mark>=90 and mark<=100:
        count1+=1
        print(f"{mark} ->Excellent")
    elif mark>=75 and mark<=89:
        count1+=1
        print(f"{mark} ->Very Good")
    elif mark>=60 and mark<=74:
        count1+=1
        print(f"{mark}->Good")
    elif mark>=40 and mark<=59:
        count1+=1
        print(f"{mark}->Average")
    elif mark>=0 and mark<=39:
        count2+=1
        print(f"{mark}->Fail")
    else:
        print(f"{mark}->Invalid")
print("Total no.of valid students is:",count1)
print("Total no.of Failed students is:",count2)


