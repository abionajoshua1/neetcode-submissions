class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_count:
                char_count[s[right]] += 1
            else:
                char_count[s[right]] = 1

            max_frequency = max(max_frequency, char_count[s[right]])

            while (right - left + 1) - max_frequency > k:
                char_count[s[left]] -= 1
                left += 1

            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length