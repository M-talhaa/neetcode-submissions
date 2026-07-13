class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {']':'[', '}':'{', ')':'('}
        for ch in s:
            if ch in close_to_open:
                if stack and close_to_open[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                 stack.append(ch)
        return True if not stack else False 
            
