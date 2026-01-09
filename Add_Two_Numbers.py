class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}

        left = 0
        max_length = 0

        for right in range(len(s)):
            current_char = s[right]
            if current_char in char_index_map and char_index_map[current_char] >= left:
                left = char_index_map[current_char] + 1
            char_index_map[current_char] = right
            max_length = max(max_length, right - left + 1)
            
        return max_length

# --- Testing the Examples ---
sol = Solution()

# Example 1
s1 = "abcabcbb"
print(f"Input: {s1} | Output: {sol.lengthOfLongestSubstring(s1)}") # Expected: 3 ("abc")

# Example 2
s2 = "bbbbb"
print(f"Input: {s2} | Output: {sol.lengthOfLongestSubstring(s2)}") # Expected: 1 ("b")

# Example 3
s3 = "pwwkew"
print(f"Input: {s3} | Output: {sol.lengthOfLongestSubstring(s3)}") # Expected: 3 ("wke")