class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            if current_sum < 0:
                current_sum = 0
                
            current_sum += num
            max_sum = max(max_sum, current_sum)
        
        return max_sum



        """ 
        optimised version :->
        class Solution(object):
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum"""