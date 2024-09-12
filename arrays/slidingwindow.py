from collections import deque
from typing import List
class SlidingWindow:
  def __init__(self) -> None:
    pass
  
  def slidingWindowMaximum(self, nums:List[int], k:int) -> List[int]:
    output=[]
    q = deque() #store index of elements
    l=r=0
    while r < len(nums):
      # check if the last element is smaller than the latest elements
      while q and nums[q[-1]] < nums[r]:
        q.pop()
      q.append(r)
      if l > q[0]:
        q.popleft()
      if (r+1) >= k:
        output.append(nums[q[0]])
        l +=1
      r +=1
        
    return output

  
  def minimumWindowSubstring(self, s:str, t:str) -> str:
    if t == "":
      return ""
    countT, window= {}, {}
    for c in t:
      countT[c] = 1+ countT.get(c, 0)
    have, need = 0, len(countT)
    res, reslen = [-1,-1], float("infinity")
    l =0
    for r in range(len(s)):
      c = s[r]
      window[c] = 1+window.get(c,0)
      if c in countT and window[c] == countT[c]:
        have += 1
      while have==need:
        if (r-l+1) < reslen:
          res = [l,r]
          reslen = r-l+1
        # remove the left most character to check for small length matched subtstring.
        window[s[l]]=-1
        if s[l] in countT and window[s[l]]  < countT[s[l]]:
          have -=1
        l +=1
    l,r = res  
    
    return s[l:r+1] if reslen != float("infinity") else ""