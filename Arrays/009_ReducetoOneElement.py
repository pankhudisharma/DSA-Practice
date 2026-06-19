class Solution:
    def minCost(self, arr):

        minimum = min(arr)

        n = len(arr)

        return minimum * (n - 1)


arr = [4, 3, 2]

obj = Solution()

print(obj.minCost(arr))