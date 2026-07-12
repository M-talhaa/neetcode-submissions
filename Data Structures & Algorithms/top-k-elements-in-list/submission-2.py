class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = Counter(nums)
        k_times = num_map.most_common(k)
        # print(k_times)
        to_return = [key for key, value in k_times]
        # print(to_return)
        return to_return