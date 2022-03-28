class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre=0
        k=sum(nums)
        for i in range(len(nums)):
            if pre==k-pre-nums[i]:
                return i
            pre+=nums[i]
        return -1
        