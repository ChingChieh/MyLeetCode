class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        htable = {}
        for idx, val in enumerate(nums):
            if (target - val) in htable:
                return [htable[target - nums[idx]], idx]
            htable[val] = idx
