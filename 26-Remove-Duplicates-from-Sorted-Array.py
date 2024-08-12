class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Initialize the second pointer
        j = 0

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        # The number of unique elements is j + 1
        return j + 1
