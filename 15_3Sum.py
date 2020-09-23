class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            # Since the input array is sorted, it is impossible to have sum==0 start with a positive number
            if nums[i] > 0: 
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                summ = nums[i] + nums[start] + nums[end]
                if summ < 0:
                    start += 1
                elif summ > 0:
                    end -= 1
                else:
                    result.append([nums[i], nums[start], nums[end]]) 
                    start += 1
                    end -=1
                    # This while loop can make sure the result will not contain duplicate element
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
        return result