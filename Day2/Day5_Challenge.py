request_values=[]
n=int(input("Enter the no of requests: "))
for i in range(n):
    request=int(input(f"Enter the request {i+1}: "))
    request_values.append(request)
low_demand=[]
high_demand=[]
moderate_demand=[]
invalid_request=[]
total_valid=0
for i in request_values:
    if i<0:
        invalid_request.append(i)
    elif i>=1 and i<=20:
        low_demand.append(i)
        total_valid+=1
    elif i>=21 and i<=50:
        moderate_demand.append(i)
        total_valid+=1
    elif i>50:
        high_demand.append(i)
        total_valid+=1
    else:
        total_valid+=1
L=17
print("Length of my full name is:",L)
PLI=L%3
if PLI==0:
    removed_count=0
    while len(low_demand)>0:
        low_demand.pop()
        removed_count+=1
elif PLI==1:
    removed_count=0
    while len(high_demand) > 0:
        high_demand.pop()
        removed_count += 1
else:
    removed_count = 0
    while len(low_demand) > 0:
        low_demand.pop()
        removed_count += 1
    while len(high_demand) > 0:
        high_demand.pop()
        removed_count += 1
    while len(invalid_request) > 0:
        invalid_request.pop()
        removed_count += 1

print("PLI is:",PLI)
print("Total valid requests:",total_valid)
print("Removed requests:",removed_count)
print("Lowed demand:",low_demand)
print("High demand:",high_demand)
print("Moderate demand:",moderate_demand)
print("Invalid requests:",invalid_request)




