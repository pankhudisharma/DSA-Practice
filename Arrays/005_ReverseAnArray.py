class Solution:
    def reverseArray(self, arr):

        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

        return arr


arr = [1, 2, 3, 4, 5]

obj = Solution()

result = obj.reverseArray(arr)

print(result)