# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        root = TreeNode(None)
        if len(A)==1:
            root.val = A[0]
            return root
        elif len(A)==0:
            return None
        mid_index = len(A)//2
        root.val = A[mid_index]
        left_tree = A[0:mid_index]
        right_tree = A[mid_index+1:]
        root.left = self.sortedArrayToBST(left_tree)
        root.right = self.sortedArrayToBST(right_tree)
        return root

s = Solution()
s.sortedArrayToBST([1,2,3])