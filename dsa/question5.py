
def max_path_sum(root):
    com_max=float('-inf')
    def recur(root):
        nonlocal com_max
        if not root:
            return 0
        l=recur(root.left)
        r=recur(root.right)
        com_max=max(l+root.val,r+root.val,l+r+root.val,root.val,com_max)
        return max(l,r,0)+root.val
    recur(root)
    return com_max


        