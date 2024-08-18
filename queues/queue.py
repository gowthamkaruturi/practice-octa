

from trees import Node


class Queue:
  def __init__(self) -> None:
    self.items = []
  
  def enque(self,item:Node) -> None:
    #  put the elements at the start
    self.items.insert(0,item)
  
  def deque(self) -> Node:
    if self.items:
      return self.items.pop()

  def is_empty(self) -> bool:
    return len(self.items) ==0

  def peek(self) -> Node:
    if self.items:
      return self.items[-1]
  
  def size_of_queue(self) -> int:
    return len(self.items)