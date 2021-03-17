from itertools import combinations, permutations


# two pointer
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        result = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                sum_3 = v + nums[j] + nums[k]
                # from pdb import set_trace; set_trace()
                # print(sum_3, i , j, k)
                if sum_3 == 0:
                    result.add((v, nums[j], nums[k]))
                    j+=1
                    k-=1
                elif sum_3 > 0:
                    k-=1
                elif sum_3 < 0:
                    j+=1
                else:
                    assert False
        return result


                    
r = Solution().threeSum([-5,1,-10,2,-7,-13,-3,-8,2,-15,9,-3,-15,13,-6,-10,5,6,11,1,13,-12,14,6,11,4,13,-14,0,11,1,10,-11,6,-11,-10,8,2,-3,-13,-6,-9,-9,-6,11,-8,-9,1,13,9,9,3,13,0,-6,1,-10,-15,3,5,3,11,-8,0,2,-11,5,-13,6,9,-11,7,8,-13,8,4,-6,14,13,-15,1,7,-5,-1,-7,5,7,-2,-3,-13,10,7,13,9,-8,-8,13,12,-6,4,7,-10,-12,-8,-8,11,11,-6,3,9,-14,-11,2,-4,-5,10,8,-13,-7,12,-10,10])
print(r)
