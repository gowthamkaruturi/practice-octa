from trees.Node import Node


class BinarySearchTree:
  
  def __init__(self, value:int) -> None:
   self.root = Node(value)
 
  def is_empty(self,node:Node) -> bool:
    return node.item == None
      
  
  def insert(self, element:int) -> None:
    if self.root is None:
     self.root = Node(element)
    else:
      self.insert_helper(self.root,element=element)
  
  
  def insert_helper(self, node:Node, element:int) -> None:
    if self.is_empty(node):
      node.item = Node(element)
    if node.item < element:
      self.insert_helper(node.left, element=element)
    if node.item > element:
      self.insert_helper(node.left, element=element)
  
  def in_order_traversal(self, root: Node, response: list[int]) -> list[int]:
    if root:
        self.in_order_traversal(root.left, response)
        response.append(root.item)
        self.in_order_traversal(root.right, response)
    return response
  
    
  def is_leaf(self, node:Node)-> bool:
    if node.left == None and node.right == None:
      return True
    return False

  def max_value(self, node:Node) -> int:
    if node.right.right == None:
      return node.item
    else:
      return self.max_value(node.right
                            )
  
      
    