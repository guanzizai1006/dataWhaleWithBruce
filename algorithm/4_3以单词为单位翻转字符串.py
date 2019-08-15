class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """       
        words = []
        for word in s[::-1].split():
            words.append(word[::-1])
        return ' '.join(words)