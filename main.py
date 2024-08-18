
from binarysearchtree.BinarySearchTree import BinarySearchTree
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
  
  tree = BinarySearchTree(4)
  tree.insert(2)
  tree.insert(8)
  tree.insert(5)
  tree.insert(10)
  print(tree.is_valid_bst(tree.root))
  
