class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        words = text.split()
        bl = set(brokenLetters)

        for w in words:
            valid = True
            for c in w:
                if c in bl:
                    valid = False
            if valid:
                res += 1

        return res
