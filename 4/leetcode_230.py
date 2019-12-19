# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def flat_tree(root_):
            if root_ == None:
                return
            
            flat_tree(root_.left)
            sort_list.append(root_.val)
            if len(sort_list) == k:
                result_.append(sort_list[-1])
                # return sort_list[-1]
            flat_tree(root_.right)
        sort_list = []
        result_ = []
        flat_tree(root)
        
        return result_[0]

    def kthSmallest(self, root: TreeNode, k: int) -> int:

        s = []
        sort_list = []
        while True:
            # root = s.pop()
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            sort_list.append(root.val)
            k -= 1
            if not k:
                return root.val
            root = root.right
            root = root.right
        #     if not s:
        #         if root:
        #             sort_list.append(root.val)
        #         break
        # return sort_list[k-1]

        

if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(2)
    tree.right = TreeNode(4)

    print(Solution().kthSmallest(tree,1))
