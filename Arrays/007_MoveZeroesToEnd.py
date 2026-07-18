class Solution:
    def pushZerosToEnd(self, arr):

        j = 0

        for i in range(len(arr)):

            if arr[i] != 0:

                arr[i], arr[j] = arr[j], arr[i]

                j += 1

        return arr


arr = [1, 2, 0, 4, 3, 0, 5, 0]

obj = Solution()

result = obj.pushZerosToEnd(arr)

print(result)