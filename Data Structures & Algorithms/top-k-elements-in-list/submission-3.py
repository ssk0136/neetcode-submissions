class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict()
        for n in nums:
            d[n]=d.get(n,0)+1
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        return list(d.keys())[:k]