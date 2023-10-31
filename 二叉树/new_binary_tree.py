class NewBinaryTree:
    def __init__(self, root=None):
        self.root = root

    def root_(self):
        if not self.root:
            return []

        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
