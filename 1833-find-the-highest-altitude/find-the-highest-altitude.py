class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        m=0
        sum=0
        for i in gain:
            sum+=i
            m=max(sum,m)
        return m