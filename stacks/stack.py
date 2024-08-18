from trees import Node
class Stack:
  
  def __init__(self)-> None:
    self.items =[]
  
  def push(self, item:Node)-> None:
    self.items.append(item)
  
  def pop(self) -> Node:
    if self.items:
      return self.items.pop()

  def is_empty(self) -> bool:
    return len(self.items) == 0

  def peek(self) -> Node:
    if self.items:
      return self.items[-1]
    
  def size(self) -> int:
    return len(self.items)