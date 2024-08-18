
from binarytree.BinaryTree import BinaryTree
from trees.Node import Node


if  __name__ == "__main__":
  
  b = BinaryTree(1)
  b.root.left = Node(2)
  b.root.right = Node(3)
  b.root.left.left = Node(4)
  b.root.left.right = Node(5)
  # b.root.right.left = Node(6)
  # b.root.right.right = Node(7)
  print(b.in_order_traversal(b.root,[]))
  print(b.level_oder_traversal(b.root))
  print(b.reverse_level_order_traversal(b.root))
  print(b.height_of_binary_tree(b.root))
  print(b.size_of_binary_tree(b.root))
  print(b.size_of_binary_tree_iterative(b.root))
  
  tree = BinaryTree(12)
  tree.root.left = Node(32)
  tree.root.right = Node(37)
  tree.root.left.left = Node(24)
  tree.root.left.right = Node(5)
  tree.root.right.left = Node(100)
  tree.root.right.right = Node(75)
  
