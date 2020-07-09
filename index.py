from typing import List

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        if len(sentence) == 0: 
            return 0
        if len(dictionary) == 0: 
            return len(sentence)

        sentence_length = len(sentence)
        dp = [0] * (sentence_length + 1)
        for i in range(0, sentence_length):
            dp[i] = dp[i - 1] + 1
            for dic in dictionary:
                if (len(dic) <= i + 1) and sentence[i + 1 - len(dic):i + 1] == dic:
                    dp[i] = min(dp[i], dp[i - len(dic)])
        
        return dp[-2]


if __name__ == "__main__":
    su = Solution()
    print(su.respace(dictionary = ["looked","just","like","her","brother"],sentence = "jesslookedjustliketimherbrother"))