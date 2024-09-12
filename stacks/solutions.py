from stack import Stack
from typing import List

class solution:
  
  def isValid(self, s:str) -> bool:
    _stack = []
    
    for letter in s:
      if letter in ["{","(","["]:
        _stack.append(letter)
      elif len(_stack)>0:
        if letter == "}":
          if _stack.pop() != "{":
            return False
        if letter == ")":
          if _stack.pop() != "(":
            return False
        if letter == "]":
          if _stack.pop() != "[":
            return False
      else:
        return False
    return len(_stack) ==0 

  def evalRPN(self, tokens:List[str]) -> int:
    stack = []
    for token in tokens:
      if token == "+":
        stack.append(stack.pop()+stack.pop())
      elif token == "-":
        second,first = stack.pop(), stack.pop()
        stack.append(first-second)
      elif token == "*":
        stack.append(stack.pop()*stack.pop())
      elif token == "/":
        second,first = stack.pop(), stack.pop()
        stack.append(int(first/second))
      else:
        stack.append(int(token))
    return stack[0]


if __name__ == "__main__":
  solution = solution()
  print(solution.isValid("[]"))
  print(solution.evalRPN(["1","2","+","3","*","4","-"]
))