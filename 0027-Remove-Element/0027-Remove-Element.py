class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr = 0

        for i in range(len(nums)):
            if nums[i] != val:
                if ptr != i:
                    nums[ptr] = nums[i]
                ptr += 1
        return ptr