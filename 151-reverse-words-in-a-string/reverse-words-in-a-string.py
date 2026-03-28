class Solution:
    def reverseWords(self, s):
        l = s.split()
        revl = l[::-1]
        return " ".join(revl)