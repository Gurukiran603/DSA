class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num                                           # all test case not passed 
                count += (1 if num == candidate else -1)
            return candidate                                                #Boyer-Moore Voting Algorithm
            """
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums) // 2:
                return num
