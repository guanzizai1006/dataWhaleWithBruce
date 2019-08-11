# LeetCode 69 
# Sqrt(x) 求平方根

# @time： 20190811

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        result = x
        while result > x / result:
            result = (result + x / result) // 2
        return int(result)


