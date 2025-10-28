from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.left:Optional["Node"] = None
        self.right:Optional["Node"] = None
        self.height = 0
        self.set_height()
        
    def set_height(self):
        left = 0 if self.left is None else self.left.height
        right = 0 if self.right is None else self.right.height
        self.height = max(left, right) + 1

    def balance_factor(self):
        left = 0 if self.left is None else self.left.height
        right = 0 if self.right is None else self.right.height
        return right - left 

    def __repr__(self):
        # return f'{self.val} h:{self.height}'
        return f'{self.val}'


class Tree:
    def __init__(self):
        self.root:Optional["Node"] = None

    def insert(self, val):
        root = self.root
        if root is None:
            self.root = Node(val)
            return
        self.root = self._insert(root, val)
        
    def _insert(self,root:Optional["Node"], val):
        if root is None:
            return Node(val)

        if val >= root.val:
            root.right = self._insert(root.right, val)
        else:
            root.left = self._insert(root.left, val)

        root.set_height()
        root = self._rebalance(root)
        return root

    def _rebalance(self, root:Node):
        balance_factor = root.balance_factor()
        if balance_factor > 1:
            # right heavy rotate left
            if root.right.balance_factor() < 0:
                root.right = self._right_rotate(root.right)
            right = self._left_rotate(root)
            return right
        elif balance_factor < -1:
            # left heavy rotate right
            if root.left.balance_factor() > 0:
                root.left = self._left_rotate(root.left)
            left = self._right_rotate(root)
            return left
        return root

    @staticmethod
    def _left_rotate(root:Node):
        right = root.right
        root.right = right.left
        right.left = root
        root.set_height()
        right.set_height()
        return right

    @staticmethod
    def _right_rotate(root:Node):
        left = root.left
        root.left = left.right
        left.right = root
        root.set_height()
        left.set_height()
        return left

    def delete(self, val):
        if self.root is None:
            print('tree is empty')
            return
        self.root = self._delete(self.root, val)

    def _delete(self, root:Node, val):
        if root is None:
            return None  

        st = []
        prev = None
        cur = root
        while cur is not None:
            st.append(cur)
            if cur.val == val:
                break
            prev = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if cur == None:
            print('not found')
            return root

        # delete node
        if cur.left is None and cur.right is None:
            # if tree only have one item 
            if prev is None:
                return None
            if val < prev.val:
                prev.left = None
            else:
                prev.right = None
            st.pop()
        else:
            # else swap with greatest successor (smallest value in right subtree)
            successor = cur.right
            while successor.left:
                successor = successor.left

            cur.val = successor.val
            cur.right = self._delete(cur.right, cur.val)
            cur.set_height()
            st.pop()
            # update correct current
            st.append(cur)

        # rebalance from stack
        while st:
            node = st.pop()
            node.set_height()
            new_node = self._rebalance(node)
            
            if st:
                parent = st[-1]
                if new_node.val < parent.val:
                    parent.left = new_node
                else:
                    parent.right = new_node
            else:
                # set new root
                root = new_node
        return root

    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, root:Node, key):
        if root is None:
            return -1
        if root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def inorder_traverse(self, root:Node):
        if root is not None:
            self.inorder_traverse(root.left)
            print(root)
            self.inorder_traverse(root.right)

    def preorder_traverse(self, root:Node):
        if root is not None:
            print(root)
            self.preorder_traverse(root.left)
            self.preorder_traverse(root.right)

    def postorder_traverse(self, root:Node):
        if root is not None:
            self.postorder_traverse(root.left)
            self.postorder_traverse(root.right)
            print(root)

    def print_tree(self):
        root = self.root
        self._print(root, 0)

    def _print(self, node, level):
        if node is not None:
            self._print(node.right, level + 1)
            print(f'{'   '*level}{node}')
            self._print(node.left, level + 1)

if __name__ == "__main__":
    t1 = Tree()
    lst = [20, 15,10,18, 30, 25,35, 27]
    # for i in lst:
    #     t1.insert(i)
    for i in [10, 15, 13, 5, 8, 20, 25, 6, 7, 4, 3, 11]:
        t1.insert(i)
    t1.print_tree()
    print()
    print('---- test search -----')
    print(t1.search(11))
    print(t1.search(12))

    print('----- test traversal ------')
    print('--- inorder -----')
    t1.inorder_traverse(t1.root)
    print('--- post-order -----')
    t1.postorder_traverse(t1.root)
    print('--- pre-order -----')
    t1.preorder_traverse(t1.root)

    print('--- test deletion ----')
    print('--- delete 11')
    t1.delete(11)
    t1.print_tree()
    print('--- delete 8')
    t1.delete(8)
    t1.print_tree()
    print('--- delete 25')
    t1.delete(25)
    t1.print_tree()
    print('--- delete 12 (not exist)')
    t1.delete(12)
    t1.print_tree()