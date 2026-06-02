# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        queue = collections.deque()
        res = 0
        queue.append((root, float('-inf')))

        while queue:
            curr, maxVal = queue.popleft()

            if curr.val >= maxVal:
                res += 1
            
            if curr.left:
                queue.append((curr.left, max(curr.val, maxVal)))
            
            if curr.right:
                queue.append((curr.right, max(curr.val, maxVal)))
                
        return res

    