# 递归实现全排列
# Leetcode 的第 46 题
# https://www.cnblogs.com/zle1992/p/8448766.html


class Solution(object):
    def __init__(self):
        self.res = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.help(nums, 0, len(nums))

        return self.res

    def help(self, a, lo, hi):
        if(lo == hi):
            self.res.append(a[0:hi])
        for i in range(lo, hi):
            self.swap(a, i, lo)
            self.help(a, lo + 1, hi)
            self.swap(a, i, lo)
    def swap(self, a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
		
		