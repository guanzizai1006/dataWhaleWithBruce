# 滑动窗口最大值

# @time：20190811
# @

class Solution:
    def maxlnWindows(self, num, size):
        # 存放准最大值的下标
        maxqueue = []
        # 存放窗口中的最大值
        maxlist = []
        n = len(num)
        # 参数检验
        if n == 0 or size == 0 or size > n:
            return maxlist
        for i in range(n):
            # 判断队首下标对应的元素，是否已经滑出窗口
            if len(maxqueue) > 0 and i - size >= maxqueue[-1]:
                maxqueue.pop(0)
            while len(maxqueue) > 0 and num[i] > num[maxqueue[-1]]:
                maxqueue.pop()
            maxqueue.append(i)
            if i >= size - 1:
                maxlist.append(num[maxqueue[0]]
        return maxlist




