class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded +=  str(len(s)) + "&" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        
        while i < len(s):
            # 1. Find the delimiter '&' to figure out where the length number ends
            j = i
            while s[j] != "&":
                j += 1
                
            # 2. Extract the length (from i up to j)
            length = int(s[i:j])
            
            # 3. Extract the actual word
            # Starts right after '&' (which is j + 1)
            # Ends at (j + 1 + length)
            word = s[j + 1 : j + 1 + length]
            strs.append(word)
            
            # 4. Jump the 'i' pointer completely over the word we just read
            # so the next loop starts at the beginning of the next length number
            i = j + 1 + length
            
        return strs

