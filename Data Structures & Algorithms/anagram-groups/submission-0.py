from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            # print(sorted_word)
            collection[sorted_word].append(word)
        return list(collection.values())