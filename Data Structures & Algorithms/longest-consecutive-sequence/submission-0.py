class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        nums = list(sorted(nums))
        print(nums)
        counter = 1
        longest_streak = 1
        for i in range(len(nums)):
            if nums[i] == nums[i-1]+1:
                counter += 1
            else:
                longest_streak = max(longest_streak, counter)
                counter = 1
        longest_streak = max(longest_streak, counter)
            
        return longest_streak
