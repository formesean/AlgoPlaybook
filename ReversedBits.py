class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = format(n, '032b')         # convert to binary
        num = "".join(reversed(num))    # reverse the binary string
        return int(num, 2)              # convert back to integer
