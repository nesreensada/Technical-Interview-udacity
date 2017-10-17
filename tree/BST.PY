class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.insertHelper(self.root,new_val)
        
    def insertHelper(self,start,new_val):
        if start is not None:
            if(new_val>start.value):
                if (start.right is not None):
                    self.insertHelper(start.right,new_val)
                else:
                    start.right=Node(new_val)
                    return
            else:
                if (start.left is not None):
                    self.insertHelper(start.left,new_val)
                else:
                    start.left=Node(new_val)
                    
        
    def search(self, find_val):
        return self.preoder_search(self.root,find_val)
        
    def preoder_search(self,start,find_val):
        if start is not None:
            if(find_val==start.value):
                return True
            elif(find_val>start.value):
                return self.preoder_search(start.right,find_val)
            else:
                return self.preoder_search(start.left,find_val)
        return False    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)