"""
Inorder traversal : you first travel left then come to right (left bottom first)
PreOder t
"""


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if self.data == data:
            return

        if data > self.data:
            # add to the right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)
        else:
            # add to left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)

    def inoder_traversal(self):

        elements = []

        if self.left:
            elements += self.left.inoder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inoder_traversal()

        return elements

    def pre_order_traversal(self):

        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def search(self, target):
        if self.data == target:
            return True

        if target < self.data:
            if self.left:
                return self.left.search(target)
            else:
                return False

        if target > self.data:
            if self.right:
                return self.right.search(target)
            else:
                return False

    def post_order_traversal(self):
        # this is wrong

        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def get_sum(self):
        total = 0

        total += self.data

        if self.left:
            total += self.left.get_sum()

        if self.right:
            total += self.right.get_sum()

        return total

    def delete_node(self, val):

        if val > self.data:
            if self.right:
                self.right.delete_node(val)

        elif val < self.data:
            if self.left:
                self.left.delete_node(val)

        else:

            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.left is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node(min_val)

        return self


def treeBuilder(elements):
    root = BSTNode(elements[0])

    for element in elements:
        root.add_child(element)

    return root


if __name__ == "__main__":
    arr = [15, 7, 12, 14, 27, 88, 20, 23]
    tree_n = treeBuilder(arr)

    print(tree_n.inoder_traversal())
    print(tree_n.pre_order_traversal())
    print(tree_n.post_order_traversal())

    print(tree_n.search(14))
    print(tree_n.search(99))
    print(tree_n.search(88))
    print(tree_n.search(0))

    print(tree_n.find_min())
    print(tree_n.find_max())

    print(tree_n.get_sum())
