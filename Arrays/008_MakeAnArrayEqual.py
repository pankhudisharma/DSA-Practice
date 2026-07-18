class Solution:

    def minOps(self, arr, x):

        max_element = max(arr)

        operations = 0

        for num in arr:

            difference = max_element - num

            if difference % x != 0:
                return -1

            operations += difference // x

        return operations


arr = [4, 4, 4, 2]
x = 2

obj = Solution()

print(obj.minOps(arr, x))