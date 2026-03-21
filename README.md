# DSA
Leetcode and GeeksforGeeks and HackerRank
# 🔹 Problem: Two Sum
# 🔗 https://leetcode.com/problems/two-sum/
# 🟢 Difficulty: Easy

# 💡 Approach:
# Use hashmap to store visited elements
# Check if target - current exists

# ⏱ Time Complexity: O(n)
# 📦 Space Complexity: O(n)

def twoSum(nums, target):
    hashmap = {}
    
    for i, num in enumerate(nums):
        diff = target - num
        
        if diff in hashmap:
            return [hashmap[diff], i]
        
        hashmap[num] = i
