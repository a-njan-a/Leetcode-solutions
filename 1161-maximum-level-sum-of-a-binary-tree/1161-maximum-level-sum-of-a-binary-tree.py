# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        visited = collections.deque([root])
        sum_arr = []

        while(visited):
            curr_level = 0

            for _ in range(len(visited)):
                temp = visited.popleft()
                curr_level += temp.val

                if temp.left:
                    visited.append(temp.left)

                if temp.right:
                    visited.append(temp.right)

            sum_arr.append(curr_level)

        ans = sum_arr.index(max(sum_arr)) + 1
        return ans
