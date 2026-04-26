import copy
def create_inventory():
    items = [
        {
            "item": "Laptop",
            "details": {
                "price": 50000,
                "stock": 10,
                "supplier": {"name": "Dell", "rating": 4.5}
            }
        },
        {
            "item": "Phone",
            "details": {
                "price": 20000,
                "stock": 25,
                "supplier": {"name": "Samsung", "rating": 4.2}
            }
        }
    ]
    return items
def apply_discount(data, roll_no):
    n = len(data)
    target_index = roll_no % n

    for i in range(n):
        if i == target_index:
            item_info = data[i]["details"]
            item_info["price"] *= 0.9
            item_info["stock"] -= 5

def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i]["details"] == modified[i]["details"]:
            unchanged += 1
        else:
            changed += 1

    return (changed, unchanged)

roll_no = int(input("Enter roll no: "))
original = create_inventory()
modified = copy.deepcopy(original)

inventory = create_inventory()
shallow_copy = copy.copy(inventory)
deep_copy = copy.deepcopy(inventory)
apply_discount(shallow_copy, roll_no)
apply_discount(deep_copy, roll_no)
shallow_result = compare_data(inventory, shallow_copy)
deep_result = compare_data(inventory, deep_copy)
print("Original Inventory:\n", inventory)
print("\nShallow Copy:\n", shallow_copy)
print("\nDeep Copy:\n", deep_copy)

print("\nSummary:")
print("Shallow Copy (changed, unchanged):", shallow_result)
print("Deep Copy (changed, unchanged):", deep_result)
