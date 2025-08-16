class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time - O(n log n) but behaves close to O(n^2) because of pop(i) 
        # space - O(1)
        
        # i=1
        # if len(intervals) <= 1:
        #     return intervals
        # intervals.sort(key = lambda x: x[0]) # O(n log n)
        # while i<len(intervals):
        #     # if i>0:
        #     if intervals[i][0] <= intervals[i-1][1]:
        #         intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
        #         intervals.pop(i) # pop current index
        #     else:
        #         i += 1
        # return intervals

        # INTUITION - its easy. scribble on a paper to get the code. but first sort the array based on start[i] value and iterate from index 1 to compare with previous values. Take a new list to store the result cause iterating & comparing would become error prone if we do in-place.
        # time - O(n log n)
        # space - O(n)

        i=1
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key = lambda x: x[0]) # O(n log n)
        merged = [intervals[0]] # start with first interval to compare with next ones.

        while i<len(intervals): # iterate from index 1 to the last
            last = merged[-1]
            if intervals[i][0] <= last[1]:
                last[1] = max(last[1], intervals[i][1]) # eg: [(1,6), (2,3)]
            else:
                merged.append(intervals[i])
            i += 1
        return merged

            