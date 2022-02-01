class Solution:
    
    def __init__(self) -> None:
        self._tri_list = [0, 1, 1]
    
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
                    self._tri_list[i-3] + self._tri_list[i-2] + self._tri_list[i-1]
                )
            return self._tri_list[n]
        else:
            return self._tri_list[n]
        