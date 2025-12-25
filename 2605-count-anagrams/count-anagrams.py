class Solution:
    def countAnagrams(self, s: str) -> int:
        x = s.split(' ') # ['too', 'hot']
        import math
        vals2 = []
        out = 1

        def func(i):
            hash = {}
            for a in i:
                hash[a] = hash.get(a, 0) + 1 # {'t':1, 'o':2}
            return hash

        def fact(i):
            if i == 1 or i == 0:
                return 1
            # f = 1
            # for m in range(1, i+1):
            #     f *= m
            return math.factorial(i)

        for i in x: 
            # func(i) # {'t': 1, 'o': 2}
            vals = func(i).values() # [1,2]
            cp = 1
            for j in vals:
                cp *= fact(j) 
            res = fact(len(i)) // cp 
            out *= res 
            out = out % (10**9 + 7)
        
        return int(out)