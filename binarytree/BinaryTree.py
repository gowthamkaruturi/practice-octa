from trees.Node import Node
from queues.queue import Queue
from stacks.stack import Stack

class BinaryTree:
    def __init__(self, root: int) -> None:
        self.root = Node(root)

    def pre_order_traversal(self, root: Node, response: list[int]) -> list[int]:
        if root:
            response.append(root.item)
            self.pre_order_traversal(root.left, response)
            self.pre_order_traversal(root.right, response)
        return response

    def in_order_traversal(self, root: Node, response: list[int]) -> list[int]:
        if root:
            self.in_order_traversal(root.left, response)
            response.append(root.item)
            self.in_order_traversal(root.right, response)
        return response

    def post_order_traversal(self, root: Node, response: list[int]) -> list[int]:
        if root:
            self.post_order_traversal(root.left, response)
            self.post_order_traversal(root.right, response)
            response.append(root.item)
        return response
      
    def level_oder_traversal(self, root:Node)-> list[int]:
      
      result = []
      q = Queue()
      q.enque(root)
      while not q.is_empty():
   
        node = q.deque()
        result.append(node.item)
        if node.left:
          q.enque(node.left)
        if node.right:
          q.enque(node.right)
      return result
    
    
    def reverse_level_order_traversal(self, root:Node) -> list[int]:
      
      result =[]
      q = Queue()
      s = Stack()
      q.enque(root)
      
      while not q.is_empty():
        node = q.deque()
        s.push(node)
        if node.right:
          q.enque(node.right)
        if node.left:
          q.enque(node.left)
      while not s.is_empty():
        stack_item = s.pop()
        result.append(stack_item.item)
      return result
  
    def height_of_binary_tree(self, root : Node) -> int:
      if root is None:
        return -1
      left_height = self.height_of_binary_tree(root.left)
      right_height = self.height_of_binary_tree(root.right)
      return 1 + max(left_height,right_height)
    
    def size_of_binary_tree(self, root : Node) -> int:
      if root is None:
        return 0

      return 1 + self.size_of_binary_tree(root.left) + self.size_of_binary_tree(root.right)
    
    def size_of_binary_tree_iterative(self, root : Node) -> int:
      if root is None:
        return 0
      s = Stack()
      s.push(root)
      size =1
      while not s.is_empty():
        element = s.pop()
        if element.left:
          size += 1
          s.push(element.left)
        if element.right:
          size += 1
          s.push(element.right)
      return size


