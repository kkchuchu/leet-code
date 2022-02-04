from typing import List


class Solution:

    def __init__(self) -> None:
        self._tri_list = [0, 1, 1]
        self._fib_list = [1, 1]

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return Solution().fib(n-1) + Solution().fib(n-2)

    def tribonacci(self, n: int) -> int:
        if n >= len(self._tri_list):
            for i in range(len(self._tri_list), n+1):
                self._tri_list.append(
                    self._tri_list[i-3] +
                    self._tri_list[i-2] + self._tri_list[i-1]
                )
            return self._tri_list[n]
        else:
            return self._tri_list[n]

    def climbStairs(self, n: int) -> int:
        if n+1 > len(self._fib_list):
            for i in range(len(self._fib_list), n+1):
                self._fib_list.append(
                    self._fib_list[i-1] + self._fib_list[i-2])
        return self._fib_list[n]

    def minCostClimbingStairs(self, cost) -> int:
        a_i = [0 for _ in range(len(cost)+1)]
        for i in range(2, len(a_i)):
            a_i[i] = min(a_i[i-1] + cost[i-1], a_i[i-2] + cost[i-2])
        return a_i[-1]
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        a = [nums[i] for i in range(len(nums))]
        a[1] = max(a[0], a[1])
        for i in range(2, len(nums)):
            a[i] = max(a[i-2] + a[i], a[i-1])
        
        return a[-1]
