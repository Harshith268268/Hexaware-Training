"""SET 2 TASK 1: BST of claim IDs and three traversals."""
class Node:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None

def insert(root, value):
    if root is None: return Node(value)
    if value < root.value: root.left = insert(root.left, value)
    elif value > root.value: root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None: return False
    if value == root.value: return True
    return search(root.left if value < root.value else root.right, value)

def traverse(root, order, out):
    if not root: return
    if order == "pre": out.append(root.value)
    traverse(root.left, order, out)
    if order == "in": out.append(root.value)
    traverse(root.right, order, out)
    if order == "post": out.append(root.value)

def build(values):
    root = None
    for value in values: root = insert(root, value)
    return root

if __name__ == "__main__":
    values = [105, 60, 150, 30, 80, 120, 175, 80]
    root = build(values)
    print("SET 2 - TASK 1: CLAIM ID BST")
    print("Input:", values)
    for order, label in [("pre","Preorder (Root-Left-Right)"),("in","Inorder (Left-Root-Right)"),("post","Postorder (Left-Right-Root)")]:
        result=[]; traverse(root, order, result); print(label + ":", result)
    print("Search 120:", "FOUND" if search(root,120) else "NOT FOUND")
    print("Search 999:", "FOUND" if search(root,999) else "NOT FOUND")
    print("Inorder gives sorted claim IDs.")
    empty=[]; traverse(build([]),"in",empty); print("Empty-input test:",empty)
    dup=[]; traverse(build([25,25,10,40]),"in",dup); print("Duplicate-ID test:",dup)
