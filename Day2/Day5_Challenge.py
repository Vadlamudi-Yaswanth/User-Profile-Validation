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
