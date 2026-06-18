class Solution:

    def removeDuplicates(self, arr):

        # If array is empty, return empty array
        if len(arr) == 0:
            return []

        # k points to the position where the next distinct element should go
        k = 1

        # Traverse from the second element onwards
        for i in range(1, len(arr)):

            # If current element is different from the previous distinct element
            if arr[i] != arr[k - 1]:
                arr[k] = arr[i]
                k += 1

        # Return only the distinct elements
        return arr[:k]

arr = [2, 2, 3, 3, 4, 4, 5]

# Create object of Solution class
obj = Solution()

# Call the method
result = obj.removeDuplicates(arr)

# Print the result
print(result)       