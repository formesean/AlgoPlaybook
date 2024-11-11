class Solution(object):
    def hammingWeight(self, n):
        num = bin(n)[2:]    # convert to binary and remove '0b'
        count = 0

        for i in range(len(num)):
            if num[i] == "1":
                count += 1  # increment count if current number is 1

        return count
