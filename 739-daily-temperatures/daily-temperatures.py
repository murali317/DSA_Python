class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # INTUITION - Same like Next Greater element, take a monotonic decreasing stack (based on temperature values)and keep appending the indices (instead of elements) to track the indices of elements to compare and move forward. Use while loop instead of 'if' condition inside for loop.
        # time - O(n) # even though there’s a nested while loop, each index is pushed/popped only once. So total no of operations is linear in the size of the input.
        # space - O(n)
    #    “We're trading space for time here — by keeping unresolved indices in a stack, we avoid a brute-force O(n^2) solution and reduce it to linear time. The stack helps us remember which days haven’t found a warmer temperature yet, and we only resolve them once a warmer day appears.” \U0001f600

        stack = [] # O(n) in W.C., if temperatures are strictly decreasing.
        n = len(temperatures)
        res = [0] * n # would be easy no need to add 0s seperately when condtn not med.
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped_ele = stack.pop()
                res[popped_ele] = i - popped_ele
            stack.append(i)
        return res