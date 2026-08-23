class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        for i in range(h_len - n_len + 1):
            window = haystack[i: i + n_len]
            if window == needle:
                return i
        return -1