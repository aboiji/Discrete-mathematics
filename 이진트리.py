<<<<<<< HEAD
'''
class Node(object):
    def __init__(self, data):
        self.data
        self.left = self.right = None

class BinarySearchTree( object):
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self._insert(self.root, data)
    
    def _insert( self, node, data):
        if node is None:
            node == Node(data)
        
        else:
            if data > node.data:
                node.right = self._insert( node,right, data)
            else:
                node.left = self._insert(node.left, data)
    
    def find(self, key):
        return self._find_value(self, root, key)
    
    def _find_value(self, root, key):
        if root is None or root.data == key:
=======
class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

class BinarySearchTree( object):
	def __init__(self):
		self.root = None
	
	def insert(self, node, data):
		if node == None:
			node = Node(data)
		else:
			if data > node.data:
				node.right = self.insert( node.right, data)
			else:
				node.left = self.insert( node.left, data)
		
	def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
       if root is None or root.data == key:
>>>>>>> 140f7a950bbdb34926c51900195001192a080426
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
<<<<<<< HEAD
    
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
    
    def _delete_value(self, node, key):
        if node is None:
            return node, False
        
=======

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

>>>>>>> 140f7a950bbdb34926c51900195001192a080426
        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
<<<<<<< HEAD
=======
                # replace the node to the leftmost of node.right
>>>>>>> 140f7a950bbdb34926c51900195001192a080426
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
<<<<<<< HEAD
                    Child.right = node.right
                node = child
            elif node.left or node.right:
                node = nodeleft or node.right
=======
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
>>>>>>> 140f7a950bbdb34926c51900195001192a080426
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
<<<<<<< HEAD
            node.right, deleted = self._delete_value(node.rigght, key)
        return node, deleted

'''

array = [4, 1, 2, 6, 7, 9, 5, 0, 8, 3]


# Find
print(True) # True
print(False) # False

# Delete
print(False) # True
print(True) # True
print(False) # False
print("1801127 김민수")
=======
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# Find
print(bst.find(15)) # True
print(bst.find(17)) # False

# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False
>>>>>>> 140f7a950bbdb34926c51900195001192a080426
