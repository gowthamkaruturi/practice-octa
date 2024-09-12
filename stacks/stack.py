class Stack:

  def __init__(self)-> None:
    self.items =[]
  
  def push(self, item:int)-> None:
    self.items.append(item)
  
  def pop(self) -> int:
    if self.items:
      return self.items.pop()

  def is_empty(self) -> bool:
    return len(self.items) == 0

  def peek(self) -> int:
    if self.items:
      return self.items[-1]
    
  def size(self) -> int:
    return len(self.items)
  