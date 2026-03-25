class Solution(object):
    def reverseVowels(self, s):
        slist = list(s)
        vowels = "aeiouAEIOU"
        
        left = 0
        right = len(slist) - 1
        
        while left < right:
            if slist[left] not in vowels:
                left += 1
            elif slist[right] not in vowels:
                right -= 1
            else:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1
        
        return "".join(slist)


'''
| Approach         | Time Complexity | Efficient? |
| ---------------- | --------------- | ---------- |
| Your nested loop | O(n²)           | ❌ Slow     |
| Two pointers     | O(n)            | ✅ Fast     |
'''
