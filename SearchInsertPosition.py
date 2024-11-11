class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26    # init a count list to represent frequency

            # or each character in the string, update the count array
            for c in s:
                # base on the ascii value of the char, increment the count
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s) # convert to a tuple

        return res.values()
