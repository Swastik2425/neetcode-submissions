class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [1] * n
        left = 1
        for i in range(n):
            temp[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1,-1,-1):
            temp[i] *= right
            right *= nums[i]
        return temp