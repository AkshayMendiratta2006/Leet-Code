class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        word_count = len(words)
        word_freq = Counter(words)
        result = []
        for i in range(word_len):
            left = i
            right = i
            seen = Counter()
            valid_words_chained = 0
            while right + word_len <= len(s):
                current_word = s[right:right + word_len]
                right += word_len
                if current_word in word_freq:
                    seen[current_word] += 1
                    valid_words_chained += 1
                    while seen[current_word] > word_freq[current_word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        valid_words_chained -= 1
                        left += word_len
                    if valid_words_chained == word_count:
                        result.append(left)
                else:
                    seen.clear()
                    valid_words_chained = 0
                    left = right
        return result