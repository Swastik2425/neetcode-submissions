from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        # 1. Count the frequency of each element
        count = Counter(nums)
        
        # 2. Create buckets where the index is the frequency
        # We need len(nums) + 1 because the max frequency could be len(nums)
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        # Populate the buckets: freq_buckets[frequency] = [element1, element2...]
        for num, freq in count.items():
            freq_buckets[freq].append(num)
            
        # 3. Gather the top k elements starting from the highest frequency
        res = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res