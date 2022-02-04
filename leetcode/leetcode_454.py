from typing import List


class Solution:

    def fourSumCount(self, nums1: List[int], nums2: List[int], 
                     nums3: List[int], nums4: List[int]) -> int:
        
        n = len(nums1)
        mp1, mp3 = {}, {}
        for i in range(n):
            for j in range(n):
                mp1.setdefault(nums1[i] + nums2[j], 0)
                mp1[nums1[i] + nums2[j]] += 1
                mp3.setdefault(nums3[i] + nums4[j], 0)
                mp3[nums3[i] + nums4[j]] += 1
                
        count = 0
        for i, j in mp1.items():
            count = count + mp1[i]* mp3.get(-i, 0)
            
        return count
