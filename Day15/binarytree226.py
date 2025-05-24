class Solution:
    def invertTree(self, root):
        def reverseNodes(node):
            if node == None:
                return
            reverseNodes(node.left)
            reverseNodes(node.right)

            hold = node.left
            node.left = node.right
            node.right = hold

        reverseNodes(root)
        return root
