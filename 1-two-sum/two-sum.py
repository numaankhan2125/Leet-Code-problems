class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        n=len(arr)
        d = {}
        for i, num in enumerate(arr):
            print(i,num)
            complement = target - num
            if complement in d:
                return [d[complement], i]
            d[num] = i
