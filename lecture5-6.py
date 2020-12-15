'''
In this lecture we cover how optimized is binary search
And how to use AVL tree concepts to balance the binary tree's height to atmost logn
'''

class Node:
    def __init__(self, val: int or float , left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1
        self.balance_factor = 0
    
    def __repr__(self):
        return '{},{},{}'.format(self.left, self.val, self.right) 

class AVL:
    def __init__(self, node):
        self.tree = node

    def __repr__(self):
        return f'{self.tree.left}(), {self.tree.val}({self.tree.height}), {self.tree.right}()'
    
    def insert(self, val, tree=None):
        if tree is None:
            tree = self.tree
        if val < tree.val:
            if tree.left is None:
                tree.left = Node(val)
            else:
                self.insert(val, tree.left)
        elif val > tree.val:
            if tree.right is None:
                tree.right = Node(val)
            else:
                self.insert(val, tree.right)
        
        tree.height = 1 + max(self.height(tree.right), self.height(tree.left))
        tree.balance_factor = self.balance_factor(tree.left) - self.balance_factor(tree.right)
        print('balance factor',tree.balance_factor)
        
        
        if tree.balance_factor > 1: #right rotation
            print(tree.left.balance_factor)
            if tree.left.balance_factor > 0: #right-right rotation
                self.tree = self.right_rotate(tree)
            if tree.left.balance_factor < 0: #right-left rotation
                temp_1 = tree.left.right
                temp_1.height += 1
                temp_2 = tree.left
                temp_2.right = temp_1.left
                temp_2.height -= 1
                temp_1.left = temp_2
                tree.left = temp_1
                self.tree = self.right_rotate(tree)
        if tree.balance_factor < -1: #left rotation
            if tree.right.balance_factor < 0: #left-left rotation
                self.tree = self.left_rotate(tree)
            if tree.left.balance_factor > 0: #left-right rotation
                temp_1 = tree.right.left
                temp_1.height += 1
                temp_2 = tree.right
                temp_2.left = temp_1.right
                temp_2.height -= 1
                temp_1.right = temp_2
                tree.right = temp_1
                self.tree = self.left_rotate(tree)
        return
    
    def right_rotate(self, tree):
        temp = tree.left
        tree.left = temp.right
        tree.height -= 1
        print('xxxx', temp)
        temp.right = tree
        return temp
    
    def left_rotate(self, tree):
        temp = tree.right
        tree.right = temp.left
        tree.height -= 1
        print('xxxx', temp)
        temp.left = tree
        return temp
    
    def height(self, tree):
        if tree is None:
            return 0
        print(tree)
        return tree.height
    
    def balance_factor(self, tree):
        if self.height(tree) == 0:
            return 0
        return self.height(tree)

nums = [5, -1, 7, 4, 6, -2, 8]
root = Node(5)
tree = AVL(root)
for i in nums:
    tree.insert(i)
print(tree)
print(root.left)
print(root.right)