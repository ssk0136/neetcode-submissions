class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=set(numbers)
        n=len(numbers)
        seen=set()
        for i in range(n):
            if numbers[i] not in seen:
                seen.add(numbers[i])
                for j in range(i+1,n):
                    if numbers[i]+numbers[j]==target:
                        return [i+1,j+1]