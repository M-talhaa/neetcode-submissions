class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            new_list[i] = prefix
            prefix *= nums[i]
        print(new_list)
        postfix = 1
        j = len(nums)-1
        while j >= 0:
            new_list[j] *= postfix
            postfix *= nums[j]
            j -= 1
        return new_list