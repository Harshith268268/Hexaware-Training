import csv
import time

with open("orders.csv", newline="", encoding="utf-8") as f:
    orders = list(csv.DictReader(f))
for o in orders:
    o["orderId"] = int(o["orderId"])
    o["customerId"] = int(o["customerId"])
    o["amount"] = float(o["amount"])

def linear_search(data, target):
    for order in data:
        if order["orderId"] == target:
            return order
    return None

def binary_search(sorted_data, target):
    low, high = 0, len(sorted_data) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_data[mid]["orderId"] == target:
            return sorted_data[mid]
        if sorted_data[mid]["orderId"] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

target = 1014
start = time.perf_counter()
print("Linear search:", linear_search(orders, target))
print(f"Linear search time: {time.perf_counter()-start:.8f} seconds")

sorted_orders = sorted(orders, key=lambda o: o["orderId"])
start = time.perf_counter()
print("Binary search:", binary_search(sorted_orders, target))
print(f"Binary search time (sorting excluded): {time.perf_counter()-start:.8f} seconds")
print("Complexity: Linear O(n); Binary O(log n) after sorting.")
