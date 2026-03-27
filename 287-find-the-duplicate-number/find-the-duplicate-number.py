class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
    
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
    """
        slow = nums[0]
        fast = nums[0]
        while True:# Step 1: detect cycle
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow