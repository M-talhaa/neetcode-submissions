class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        s = s.lower()
        s = re.sub(r'[^\w]', '', s)
        for i in range(len(s)-1, -1, -1):
            reverse+= s[i]
        if s == reverse:
            return True
        return False