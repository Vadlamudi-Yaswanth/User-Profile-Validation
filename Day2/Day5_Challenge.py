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
