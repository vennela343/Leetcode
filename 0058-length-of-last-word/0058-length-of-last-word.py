class Solution:
    @staticmethod
    def lengthOfLastWord(s: str) -> int:
        words = s.strip().split()
        return len(words[-1]) if words else 0
