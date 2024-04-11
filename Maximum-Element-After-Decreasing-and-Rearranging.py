class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # arr[0] == 1
        # abs(arr[i] - arr[i - 1]) <= 1

        # Decrease value of elements arr to smaller >0 val

        # Rearrange elements arr in any order
        arr = sorted(arr)
        size = len(arr)
        j = 0

        arr[0] = 1 
        
        for i in range(size -1):
            j += 1
            if arr[j] == (arr[i] or (arr[i] - 1)):
                continue
            else:
                arr[j] = arr[i] + 1

        return max(arr)
