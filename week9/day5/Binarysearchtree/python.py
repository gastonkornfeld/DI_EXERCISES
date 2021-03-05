
# Part 1: The Binary Tree
# Let’s start by implementing a representation of a binary tree (a tree where every 
# node has at most two children), a tree is represented by its root node.
# Create a class Node, it has three attributes, left, right and value, respectively
#  its left and right child and its value, the children can be None.
# Then add the basic methods to this class: get_left(), get_right(), set_left(node), set_right(node), 
# set_value(value) and get_value().


# Part 2: The Binary Search Tree
# Now let’s transform this binary tree into a binary search tree, 
# implement a function add_node(node) and add it to the three, 
# make sure you respect all the conditions of the binary search tree 
# (the node needs to be added at the right place, depending on its value).



# Part 3: Use The Binary Search Tree
# Implement a method search(value) which return the node containing this value inside the tree.

    


class Node():
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        self.left_side = "0(" + str(self.value) + ")00("
        self.right_side = "0(" + str(self.value) + ")01("
    
    def __repr__(self):
        return str(self.value)

    def add_node(self, other):
        # node_value = node_to_add.get_value()
        # left_value = node_to_add.get_left()
        # right_value = node_to_add.get_right()
        # print(node_value, left_value, right_value)
        # first compare with the parent node then with the others
        # if self.value:
                      
        if other.value > self.value:
            if self.right == None:
                self.right = Node(other)
                
            else:
                self.right.add_node(other)
        elif other.value < self.value:
            if self.left == None:
                self.left = Node(other)
            else:
                self.left = add_node(other) 
    

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()


    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, new_value):
        self.left = new_value

    def set_right(self, new_value):
        self.right = new_value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value


parent_node = Node(55)
child1 = Node(22)
child2 = Node(88)
child3 = Node(34)
child4 = Node(78)
child5 = Node(123)
child6 = Node(56)
child7 = Node(1)
child8 = Node(6)
# print(child1)
parent_node.add_node(child1)
parent_node.add_node(child2)
child1.add_node(child3)
child1.add_node(child7)
parent_node.PrintTree()
child1.PrintTree()




# parent_node.add_node(child2)
# parent_node.add_node(child3)
# parent_node.add_node(child4)
# parent_node.add_node(child5)
# parent_node.add_node(child6)
# parent_node.add_node(child7)
# parent_node.add_node(child8)




# child3 = Node(26)
# child4 = Node(29)
# child5 = Node(30)
# child6 = Node(33)
# child7 = Node(2)
# parent_node = Node(33, child1, child2)
# print(parent_node)
# print(list_of_nodes)


