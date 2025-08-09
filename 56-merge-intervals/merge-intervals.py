class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # INTUITION - its easy. scribble on a paper to get the code. but first sort the array based on start[i] value and iterate from index 1 to compare with previous values.
        # time - 
        i=1
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        while i<len(intervals):
            # if i>0:
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i) # pop current index
            else:
                i += 1
        return intervals