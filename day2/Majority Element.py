class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in set(nums):
            s=nums.count(i)
            if s>len(nums)//2:
                return i
            