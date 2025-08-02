class Solution:
    def myAtoi(self, s: str) -> int:
        # INTUITION - first remove leading spaces -> find out sign and store it in a var to multily with result later -> loop through the chars & parse -> multiply the sign -> check if the res is in range or not and return accordingly.
        # time - O(n)
        # space - O(1)
        
        s = s.lstrip() # trimming the leading spaces
        sign = 1 # going to change depending on + or -
        i = 0
        if i < len(s) and s[i] == '+':
            i += 1 # just move forward
        elif i < len(s) and s[i] == '-':
            sign = -1 # we'll multiple the result with this later.
            i += 1
        
        parsed = 0
        while i < len(s): # i continues from where it left above, not from index 0.
            if not s[i].isdigit():
                break
            else:
                parsed = parsed * 10 + int(s[i])
            i += 1

        parsed *= sign
        if parsed < -2**31:
            return -2**31
        elif parsed >= 2**31 - 1:
            return 2**31 - 1
        else:
            return parsed

