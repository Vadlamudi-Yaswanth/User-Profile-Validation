transaction_list=[]
n=int(input("Enter the no.of transactions: "))
for i in range(n):
    transaction_amount=int(input(f"Enter the {i+1} transaction amount: "))
    transaction_list.append(transaction_amount)
categories = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}
for i in transaction_list:
    if i<=0:
        categories["invalid"].append(i)
    elif 1<=i<=500:
        categories["normal"].append(i)
    elif 501<=i<=2000:
        categories["large"].append(i)
    else:
        categories["high_risk"].append(i)

total=sum([t for t in transaction_list if t>0])
frequent_transactions_observed=False
large_spending=False
suspicious_pattern_identified=False
if n>5:
    frequent_transactions_observed=True
if total>5000:
    large_spending=True
if len(categories["high_risk"])>=3:
    suspicious_pattern_identified=True
transaction_tuple=(total, n, len(categories["high_risk"]))
if suspicious_pattern_identified or (frequent_transactions_observed and large_spending):
    risk = "High Risk"
elif frequent_transactions_observed or large_spending:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"
print("Categorized Transactions:")
print(categories)
print("\nTotal Transaction Value:", transaction_tuple[0])
print("Number of Transactions:", transaction_tuple[1])
print("Risk:", risk)

