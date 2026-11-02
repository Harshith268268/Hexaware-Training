from collections import deque
import csv

with open("orders.csv", newline="", encoding="utf-8") as f:
    orders = list(csv.DictReader(f))
order_ids = [int(o["orderId"]) for o in orders]

class CustomStack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None

class CustomQueue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0) if self.items else None

stack = CustomStack()
for item in order_ids[:3]:
    stack.push(item)
stack.pop()  

built_in_stack = []
for item in order_ids[:3]:
    built_in_stack.append(item)
built_in_stack.pop()

queue = CustomQueue()
for item in order_ids[:3]:
    queue.enqueue(item)
queue.dequeue()  

built_in_queue = deque(order_ids[:3])
built_in_queue.popleft()

print("Custom stack after undo:", stack.items)
print("Built-in list stack after undo:", built_in_stack)
print("Custom queue after dispatch:", queue.items)
print("Built-in deque queue after dispatch:", list(built_in_queue))
print("Complexity: Stack push/pop O(1) amortized; custom list queue dequeue O(n); deque operations O(1).")
