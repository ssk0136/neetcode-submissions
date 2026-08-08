class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(n)):
            complement = target - n[i]

            if complement in d:
                return [d[complement], i]

            d[n[i]] = i