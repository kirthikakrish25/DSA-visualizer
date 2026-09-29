class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    # ==========================================
    # INSERT
    # ==========================================

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):

        if node is None:
            return TreeNode(data)

        if data < node.data:
            node.left = self._insert(node.left, data)

        elif data > node.data:
            node.right = self._insert(node.right, data)

        # Duplicate values are ignored
        return node

    # ==========================================
    # SEARCH
    # ==========================================

    def search(self, data):

        current = self.root

        while current is not None:

            if data == current.data:
                return True

            elif data < current.data:
                current = current.left

            else:
                current = current.right

        return False

    # ==========================================
    # SEARCH STEPS
    # ==========================================

    def search_steps(self, target):

        steps = []

        current = self.root

        while current is not None:

            steps.append({
                "value": current.data,
                "message": f"Checking node {current.data}"
            })

            if target == current.data:

                steps.append({
                    "value": current.data,
                    "message": f"{target} found!"
                })

                return steps

            elif target < current.data:

                steps.append({
                    "value": current.data,
                    "message": (
                        f"{target} < {current.data}, "
                        "move to the left subtree"
                    )
                })

                current = current.left

            else:

                steps.append({
                    "value": current.data,
                    "message": (
                        f"{target} > {current.data}, "
                        "move to the right subtree"
                    )
                })

                current = current.right

        steps.append({
            "value": None,
            "message": f"{target} not found in the tree."
        })

        return steps

    # ==========================================
    # DELETE
    # ==========================================

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):

        # Value not found
        if node is None:
            return None

        # Search left subtree
        if data < node.data:

            node.left = self._delete(
                node.left,
                data
            )

        # Search right subtree
        elif data > node.data:

            node.right = self._delete(
                node.right,
                data
            )

        # Node found
        else:

            # ----------------------------------
            # CASE 1: NO CHILDREN
            # ----------------------------------

            if node.left is None and node.right is None:
                return None

            # ----------------------------------
            # CASE 2: ONLY RIGHT CHILD
            # ----------------------------------

            if node.left is None:
                return node.right

            # ----------------------------------
            # CASE 2: ONLY LEFT CHILD
            # ----------------------------------

            if node.right is None:
                return node.left

            # ----------------------------------
            # CASE 3: TWO CHILDREN
            # ----------------------------------

            successor = self._find_min(node.right)

            node.data = successor.data

            node.right = self._delete(
                node.right,
                successor.data
            )

        return node

    # ==========================================
    # FIND MINIMUM
    # ==========================================

    def _find_min(self, node):

        current = node

        while current.left is not None:
            current = current.left

        return current

    # ==========================================
    # INORDER
    # ==========================================

    def inorder(self):

        result = []

        def traverse(node):

            if node is not None:

                traverse(node.left)

                result.append(node.data)

                traverse(node.right)

        traverse(self.root)

        return result

    # ==========================================
    # PREORDER
    # ==========================================

    def preorder(self):

        result = []

        def traverse(node):

            if node is not None:

                result.append(node.data)

                traverse(node.left)

                traverse(node.right)

        traverse(self.root)

        return result

    # ==========================================
    # POSTORDER
    # ==========================================

    def postorder(self):

        result = []

        def traverse(node):

            if node is not None:

                traverse(node.left)

                traverse(node.right)

                result.append(node.data)

        traverse(self.root)

        return result

    # ==========================================
    # HEIGHT
    # ==========================================

    def height(self):

        def get_height(node):

            if node is None:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            return 1 + max(
                left_height,
                right_height
            )

        return get_height(self.root)

    # ==========================================
    # COUNT NODES
    # ==========================================

    def count_nodes(self):

        def count(node):

            if node is None:
                return 0

            return (
                1
                + count(node.left)
                + count(node.right)
            )

        return count(self.root)


# =================================================
# TESTING
# =================================================

if __name__ == "__main__":

    tree = BinarySearchTree()

    # Create BST
    values = [
        50,
        30,
        70,
        20,
        40,
        60,
        80
    ]

    for value in values:
        tree.insert(value)

    print("Initial tree")
    print("====================")

    print("Inorder:")
    print(tree.inorder())

    print("\nPreorder:")
    print(tree.preorder())

    print("\nPostorder:")
    print(tree.postorder())

    print("\nSearch 40:")
    print(tree.search(40))

    print("\nSearch 100:")
    print(tree.search(100))

    print("\nSearch steps for 60:")

    steps = tree.search_steps(60)

    for step in steps:
        print(step["message"])

    print("\nHeight:")
    print(tree.height())

    print("\nNumber of nodes:")
    print(tree.count_nodes())

    # =================================================
    # DELETE TEST
    # =================================================

    print("\n====================")
    print("DELETE TEST")
    print("====================")

    print("\nBefore deletion:")
    print(tree.inorder())

    # Delete leaf node
    tree.delete(20)

    print("\nAfter deleting 20:")
    print(tree.inorder())

    # Delete node with one child / leaf depending on current tree
    tree.delete(30)

    print("\nAfter deleting 30:")
    print(tree.inorder())

    # Delete node with two children
    tree.delete(50)

    print("\nAfter deleting 50:")
    print(tree.inorder())