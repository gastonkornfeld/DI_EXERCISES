
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
    number_of_node = 0
    list_of_nodes = []
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.id = Node.number_of_node
        Node.number_of_node += 1
        Node.list_of_nodes.append(self)
        
        self.left_side = "0(" + str(self.value) + ")00("
        self.right_side = "0(" + str(self.value) + ")01("
    
    def __repr__(self):
        return str(self.value)

    def add_node(self, value):
        
        if self.value:
                      
            if value > self.value:
                if self.right == None:
                    self.right = Node(value)
                    
                else:
                    self.right.add_node(value)
            elif value < self.value:
                if self.left == None:
                    self.left = Node(value)
                else:
                    self.left.add_node(value) 
        else:
            self.value = value        

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()

    def search(self, number):
        for node in Node.list_of_nodes:
            if node.value == number:
                print(f"node id {node.id}")


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

# print(child1)
parent_node.add_node(12)
parent_node.add_node(6)
parent_node.add_node(14)
parent_node.add_node(3)

parent_node.add_node(122)
parent_node.add_node(63)
parent_node.add_node(124)
parent_node.add_node(35)
parent_node.PrintTree()
parent_node.search(14)

node1 = Node(22)
node1.add_node(12)
node1.add_node(24)
parent_node.search(3)





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
# parent_node = Node(33)
# print(parent_node)
# print(list_of_nodes)


