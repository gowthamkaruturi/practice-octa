from trees.Node import Node


class BinarySearchTree:
  
  def __init__(self, value:int) -> None:
   self.root = Node(value)
 
  def is_empty(self,node:Node) -> bool:
    if not node:
      return True
    return node.item == None
      
  
  def insert(self, element:int) -> None:
    if self.root is None:
     self.root = Node(element)
    else:
      self.insert_helper(self.root,element=element)
  
  
  def insert_helper(self, node:Node, element:int) -> None:

    if node.item < element:
      if node.right is None:
        node.right = Node(element)
      else:
        self.insert_helper(node.right, element=element)
    else :
      if node.left is None:
        node.left = Node(element)
      else:
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
    if node.right == None:
      return node.item
    else:
      return self.max_value(node.right
                            )
  
  def min_value(self, node:Node) -> int:
    if node.left == None:
      return node.item
    else:
      return self.min_value(node.left)
  
  def is_valid_bst(self) -> bool:
    return self.helper(self.root, inf
                       )
    
  
  def helper(self,node:Node, min:int,max:int)-> bool:
    
    if not node:
      return True
    if node.left.item <= min or node.right.item >= max:
     return False
    else:
      return self.helper(node.left,min,node.item) and self.helper(node.right,node.item, max)
    