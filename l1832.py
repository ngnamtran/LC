class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        count = [0] * 26
        for c in sentence:
            if 'a' <= c <= 'z':
                count[ord(c) - ord('a')] += 1
        return all(c > 0 for c in count)
