

class Node:
    def __init__(self, code):
        self.code = code
        self.left = None
        self.right = None


def insert(root, code):
    if root is None:
        return Node(code)
    if code < root.code:
        root.left = insert(root.left, code)
    elif code > root.code:
        root.right = insert(root.right, code)
    
    return root


def search(root, target):
    if root is None:
        return False
    if target == root.code:
        return True
    if target < root.code:
        return search(root.left, target)
    return search(root.right, target)


def height(root):
    """Height measured in number of nodes; empty tree has height 0."""
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.code)
        inorder(root.right, result)


def main():
   
    hub_codes = [50, 30, 70, 20, 40, 60, 80]
    root = None

    print("SET 3 - TASK 1: BST HUB DIRECTORY")
    print("Insertion order:", hub_codes)
    for code in hub_codes:
        root = insert(root, code)

    sorted_codes = []
    inorder(root, sorted_codes)
    print("Hub codes in sorted order (inorder):", sorted_codes)
    print("Tree height:", height(root), "levels")

    target = 60
    print(f"Search for hub {target}:", "FOUND" if search(root, target) else "NOT FOUND")

    sorted_input = [10, 20, 30, 40, 50, 60, 70]
    sorted_root = None
    for code in sorted_input:
        sorted_root = insert(sorted_root, code)
    print("\nSorted insertion order:", sorted_input)
    print("Height after sorted insertion:", height(sorted_root), "levels")
    print("Explanation: inserting sorted values into an ordinary BST makes it")
    print("skewed like a linked list, increasing height and worst-case operations.")
    print("A balanced BST (such as AVL or Red-Black) avoids this problem.")


if __name__ == "__main__":
    main()
