
from binarytree.BinaryTree import BinaryTree
from trees.Node import Node


if  __name__ == "__main__":
  
  b = BinaryTree(1)
  b.root.left = Node(2)
  b.root.right = Node(3)
  b.root.left.left = Node(4)
  b.root.left.right = Node(5)
  b.root.right.left = Node(6)
  b.root.right.right = Node(7)
  print(b.in_order_traversal(b.root,[]))