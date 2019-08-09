# Leetcode 系列习题

# 1. 第20题， 有效的括号
class Solution():
    def isValid(self, s):
        stack = []
        dic = {')':'(', '}':'{',']':'['}
        for char in s:
            if char in dic.values():
                stack.append(char)
            elif char in dic.keys():
                if stack == [] or dic[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


# 2. 第32题， 最长有效括号
def longestValidParentheses():
    l = 0
    stack = []
    start = 0
    dic = {')':'('}
    for i in range(len(s)):
        if s[i] in dic.values():
            stack.append(s[i])
        elif s[i] in dic.keys():
            if stack == []:
                i += 1
                continue
            if s[i] != stack.pop():
                l += 2
        else:
            return 0
        i += 1
    return l

# 3. 第150题， 逆波兰表达式求值 
def evalRPN(tokens):
    stack = list()
    oper = ['+', '-', '*', '/']
    for char in tokens:
        if char not in oper:
            stack.append(int(char))
        else:
            top1 = stack.pop()
            top2 = stack.pop()
            if char == '+':
                stack.append(top2 + top1)
            elif char == '-':
                stack.append(top2 - top1)
            elif char == '*':
                stack.append(top2 * top1)
            elif char == '/':
                stack.append(int(top2/top1))
    return stack.pop()




