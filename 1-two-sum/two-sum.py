class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]

            seen[nums[i]] = i



'''Approach	   Time	   Space
Brute Force	    O(n²)	O(1)
HashMap (Best)	 O(n)	O(n)'''
