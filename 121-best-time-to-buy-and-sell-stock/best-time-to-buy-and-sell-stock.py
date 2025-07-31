class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # nested looping technique - not suitable for larger data & inefficient
        # time - O(n^2) space - O(1)

        # md = 0
        # for i in range(len(prices)-1):
        #     for j in range(i, len(prices)):
        #         if prices[j] - prices[i] > 0 and prices[j] - prices[i] > md:
        #             md = prices[j] - prices[i]
        # return md

        # This Brute-force gives Time Limit Exceeded for large inputs. 
        # time - O(n^2) space - O(1)

        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i] 
        #         max_profit = max(max_profit, profit)
        # return max_profit


        # Implementing Greedy Approach.... This is a way of storing/ keep tracking of min_price & max_price to compare it with the later ones.
        # We calculate profit dynamically and keep updating max_profit.
        # We never go back—this is why Greedy works well here.
        # time - O(n) space - O(1)

        # max_profit = 0
        # min_profit = float('inf')
        # for i in prices:
        #     min_profit = min(min_profit, i)
        #     max_profit = max(max_profit, i-min_profit)
        # return max_profit

        # KADANE'S ALGORITHM (1D DP approach) --------
        # INTUITION - fix 1 pointer at 0th index, keep checking upcoming elements < that element, if yes movethat pointer there. Else if check upcoming elements - this element diff > profit. IF yes, update the profit and return.
        # time - O(n) space - O(1)

        buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > max_profit:
                max_profit = prices[i] - buy
        return max_profit


