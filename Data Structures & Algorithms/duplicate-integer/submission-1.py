class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in c:
                return True
            c.add(nums[i])
        return False