class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # time - O(n^2 * (m + n) log(m + n)) due to repeated sorting inside loops - highly inefficient.
        # space - O(m+n) as it creates a new list

        # nums1 = nums1[:m:]+nums2 # O(m+n) time & space
        # for i in nums1[m::]: # O(n)
        #     for j in nums2: # O(n)
        #         i=j
        #         nums1.sort() # O((m + n) log(m + n))   


        # INTUITION - think of why they gave m, n. It is to use them. And the empty space in nums1 is at last, so why not go from the last to as its not possible to insert element from front which overwrites valid data. Take 2 pointers (m-1, n-1) and a loop (m+n-1)
        # time - O(m + n) - single pass through both arrays, any element is not revisited.
        # space - O(1)

        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0: # does up to m + n iterations # but if there would be a nested loop inside this, it could lead to O(m*n)
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1  # \U0001f511 move the pointer for merged array!

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        
