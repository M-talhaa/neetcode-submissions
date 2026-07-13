class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        s = s.lower()
        s = re.sub(r'[^\w]', '', s)
        s = "".join(s)
        print(s)
        for i in range(len(s)-1, -1, -1):
            reverse+= s[i]
        print(reverse)
        if s == reverse:
            return True
        return False