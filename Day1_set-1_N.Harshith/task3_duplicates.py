import csv

with open("orders.csv", newline="", encoding="utf-8") as f:
    orders = list(csv.DictReader(f))
for o in orders:
    o["customerId"] = int(o["customerId"])
    o["amount"] = float(o["amount"])

seen = set()
duplicates = set()
for order in orders:
    pair = (order["customerId"], order["amount"])
    if pair in seen:
        duplicates.add(pair)
    else:
        seen.add(pair)

print("Duplicate (customerId, amount) pairs:")
for pair in sorted(duplicates):
    print(pair)
print("Complexity: Average time O(n); space O(n).")
print("For a real one-minute rule, parse createdAt and compare timestamps; this sample demonstrates repeated pairs.")
