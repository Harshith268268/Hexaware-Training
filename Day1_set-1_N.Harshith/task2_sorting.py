import csv

with open("orders.csv", newline="", encoding="utf-8") as f:
    orders = list(csv.DictReader(f))
for o in orders:
    o["orderId"] = int(o["orderId"])
    o["customerId"] = int(o["customerId"])
    o["amount"] = float(o["amount"])

def bubble_sort_desc(data):
    result = data.copy()
    n = len(result)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if result[j]["amount"] < result[j + 1]["amount"]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def merge_sort_desc(data):
    if len(data) <= 1:
        return data.copy()
    mid = len(data) // 2
    left = merge_sort_desc(data[:mid])
    right = merge_sort_desc(data[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["amount"] >= right[j]["amount"]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

bubble = bubble_sort_desc(orders)
merge = merge_sort_desc(orders)
builtin = sorted(orders, key=lambda o: o["amount"], reverse=True)

print("Bubble sort top 5:", [(o["orderId"], o["amount"]) for o in bubble[:5]])
print("Merge sort top 5:", [(o["orderId"], o["amount"]) for o in merge[:5]])
print("Built-in sort top 5:", [(o["orderId"], o["amount"]) for o in builtin[:5]])
print("Bubble sort matches built-in:", [(o["orderId"], o["amount"]) for o in bubble] == [(o["orderId"], o["amount"]) for o in builtin])
print("Merge sort matches built-in:", [(o["orderId"], o["amount"]) for o in merge] == [(o["orderId"], o["amount"]) for o in builtin])
print("Complexity: Bubble O(n^2); Merge O(n log n); built-in sort O(n log n) worst case.")
print("Paper trace tip: Bubble sort first pass moves the largest amount to the first position for this descending comparison.")
