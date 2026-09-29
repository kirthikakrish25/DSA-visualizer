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
    # INORDER TRAVERSAL
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
    # PREORDER TRAVERSAL
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
    # POSTORDER TRAVERSAL
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


# ==========================================
# TESTING
# ==========================================

if __name__ == "__main__":

    tree = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        tree.insert(value)

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

    print("\nHeight:")
    print(tree.height())

    print("\nNumber of nodes:")
    print(tree.count_nodes())