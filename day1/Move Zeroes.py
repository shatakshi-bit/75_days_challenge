class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        v=nums.count(0)
        while(nums.count(0)):
            nums.remove(0)
        for i in range(v):
            nums.append(0)
        