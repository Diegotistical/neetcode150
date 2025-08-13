<<<<<<< HEAD:01. Arrays and Hashing/topk_frequent_elements.py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
=======
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
>>>>>>> 14937b248966e180ac7ad33286ee8647487739f1:Arrays and Hashing/topk_frequent_elements.py
                    return res