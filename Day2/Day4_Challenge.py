activity_scores=[]
n=int(input("Enter the number of students:"))
for i in range(n):
    score=int(input("Enter the student score:"))
    activity_scores.append(score)
low_risk=[]
medium_risk=[]
high_risk=[]
critical_risk=[]
ignored_count=0
for score in activity_scores:
    if score>=0 and score<=30:
        low_risk.append(score)
    elif score>=31 and score<=60:
        medium_risk.append(score)
    elif score>=61 and score<100:
        high_risk.append(score)
    elif score>=100:
        critical_risk.append(score)
    else:
        ignored_count+=1
print("Register Digit(D):",7)
print("Lowe Risk:",low_risk)
print("Medium Risk:",medium_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critical_risk)
print("After Personalized Filtering:")
print("Lowe Risk:",low_risk)
print("Medium Risk:",medium_risk)
print("High Risk:",high_risk)
removed_count = 0
while len(critical_risk) > 0:
    critical_risk.pop()
    removed_count = removed_count + 1
print("Critical Risk:",critical_risk)
print("Critical Risk:",critical_risk)
print("Total valid Entries:",n-ignored_count)
print("Total Ignored Entries:",ignored_count)
print("Removed Due to Personalization:",removed_count)



