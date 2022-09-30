# Binary Tree

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def create(self):
        self.data = 0
        
        self.left = Tree(1)
        self.right = Tree(2)
        
        self.left.left = Tree(3)
        self.left.right = Tree(4)
        
        self.right.left = Tree(5)
        self.right.right = Tree(6)
        
        self.right.left.left = Tree(7)
        self.right.left.left.left = Tree(8)
        
        self.left.right.right = Tree(9)
        
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
        
    def inorder(self, ptr):
        if ptr == None:
            return
        else:
            self.inorder(ptr.left)
            print(ptr.data)
            self.inorder(ptr.right)
            
    def preorder(self, ptr):
        if ptr == None:
            return
        else:
            print(ptr.data)
            self.preorder(ptr.left)
            self.preorder(ptr.right)
    
    def postorder(self, ptr):
        if ptr == None:
            return
        else:
            self.postorder(ptr.left)
            self.postorder(ptr.right)
            print(ptr.data)
            
myTree = Tree(0)
myTree.create()
myTree.display()
# myTree.postorder(myTree)