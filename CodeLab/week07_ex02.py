class Bstree:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        
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
            print(ptr.data, end=' ')
            self.inorder(ptr.right)
            
    def insert(self, val):
        if self.data == val:
            return
        elif val > self.data:
            # go to right
            if self.right == None:
                self.right = Bstree(val)
            else:
                self.right.insert(val)
        else: # val < self.data
            # go to left
            if self.left == None:
                self.left = Bstree(val)
            else:
                self.left.insert(val)
                
    def findMax(self):
        if self.left == None and self.right == None:
            max = self.data
            self.data = -1
            return max
        elif self.right == None:
            return self.left.findMax()
        elif self.left == None:
            return self.right.findMax()
        else:
            return self.right.findMax()
    
    def clearNode(self, val):
        if self.left != None and self.left.data == val:
            self.left = None
        elif self.right != None and self.right.data == val:
            self.right = None
        else:
            self.right.clearNode(val)
    
    def delete(self, val):
        if self.data == val:
            print('found {}'.format(val))
            # find max of left node
            max = self.left.findMax()
            print('max = {}'.format(max))
            
            self.data = max
            self.left.clearNode(-1)
        elif val < self.data:
            if self.left != None:
                self.left.delete(val)   
        elif val > self.data:
            if self.right != None:
                self.right.delete(val)
    
# bst = Bstree(5)

# bst.left = Bstree(3)
# bst.right = Bstree(10)
# bst.display()

# print('insert ...6')
# bst.insert(6)
# bst.display()

# bst.inorder(bst)

data = [8,5,6,9,2,1,4,7]
bst = Bstree(data[0])
for d in data:
    bst.insert(d)
bst.display()
bst.delete(5)
bst.display()