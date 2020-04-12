class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node == None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)

def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)


node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')
node_g = Node('G')

node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

print('#'*5 + ' PREORDER ' + '#'*5)
print('ROOT -> LEFT -> RIGHT')
preorder(node_a)

print('#'*5 + ' INORDER ' + '#'*5)
print('LEFT -> ROOT -> RIGHT')
inorder(node_a)

print('#'*5 + ' POSTORDER ' + '#'*5)
print('LEFT -> RIGHT -> ROOT')
postorder(node_a)
