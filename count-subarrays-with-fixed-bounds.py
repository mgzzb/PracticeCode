

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        lastMin = lastMax = lastInvalid = -1

        for idx, num in enumerate(nums):

            if num == minK:
                lastMin = idx

            if num == maxK:
                lastMax = idx

            if num < minK or num > maxK:
                lastInvalid = idx

            if lastMin > lastInvalid and lastMax > lastInvalid:
                count += min(lastMin, lastMax) - lastInvalid

        return count
