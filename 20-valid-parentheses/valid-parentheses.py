class Solution:
    def isValid(self, s: str) -> bool:
        # INTUITION - Take a hashmap of closed -> open brackets. Iterate over 's', compare the items with previously added open brackets in stack by popping them and return.
        # Time - O(n) - we iterate over the string once.
        # Space - O(n) - could be O(k) which is no of opening brackets in 's', but in W.C., all brackets of 's' could be open.
        
        stack = []
        hashing = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in hashing:
                top_ele = stack.pop() if stack else '#' # it means when any bracket compared with '#' it automatically returns False as they cant be same. 
                if hashing[i] != top_ele:
                    return False
            else:
                stack.append(i) # appending the opening brackets.
        return not stack # if empty is stack means we have processed all the open brackets so True. Otherwise False

        # ALTERNATE APPROACH ------------
        hash = {')': '(', ']': '[', '}': '{'}
        a = []

        if len(s) == 1:
            return False
        
        if s[0] in hash:
            return False

        for i in s:
            if i not in hash:
                a.append(i)
            elif not a:
                return False
            elif a and hash[i] != a.pop():
                return False
        return True if not a else False
                
            


