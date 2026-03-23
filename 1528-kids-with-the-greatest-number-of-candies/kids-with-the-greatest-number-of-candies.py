class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]




class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        max_candies = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
