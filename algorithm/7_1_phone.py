# 给定一个数字字符串，返回该数字可能代表的所有可能的字母组合。 
# 下面给出了数字到字母的映射（就像在电话按钮上一样）
# 递归，实现  http://www.luyixian.cn/news_show_20544.aspx

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        def dfs(num, string, res):
            if num == length:
                res.append(string)
                return
            for letter in dict[digits[num]]:
                    dfs(num+1, string+letter, res)
        
        dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        res = []
        length = len(digits)
        dfs(0, '', res)
        return res