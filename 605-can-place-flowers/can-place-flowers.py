class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        
        while i < len(flowerbed):
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i-1] == 0) and
                (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):
                
                flowerbed[i] = 1
                n -= 1
                
                if n == 0:
                    return True
                
                i += 2  # move 2 steps after planting
            else:
                i += 1  # always move forward
        
        return n <= 0