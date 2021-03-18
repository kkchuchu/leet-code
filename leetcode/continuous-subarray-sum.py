class Solution:
    def checkSubarraySum(self, nums, k: int):
        n = len(nums)
        for i in range(n):
            a = nums[i]
            for j in range(i+1, n):
                a = (a+nums[j])
                if k != 0:
                    a = a%k
                if a == 0:
                    return True
        return False
    
    
print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6))
print(Solution().checkSubarraySum([23,2,6,4,7], 0))
print(Solution().checkSubarraySum([0,0], 0)) # true
print(Solution().checkSubarraySum([0,1,0], 0)) # false
print(Solution().checkSubarraySum([23,2,4,6,7], -6
