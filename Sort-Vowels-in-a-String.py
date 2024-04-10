'''
Runtime:
Memory:
'''
class Solution:
    def sortVowels(self, s: str) -> str:
        size = len(s)
        t = [0]*size
        v = []

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i in range(size):
            if s[i] not in vowels:
                t[i] = s[i]
            else:
                v.append(s[i])
                
        if len(v)>0:
            v = sorted(v)
            v = v[::-1]


        for i, val in enumerate(t):
            if val == 0:
                t[i] = v.pop()
        
        # Vowels sorted in increasing order ASCII

        # return string
        return ''.join(t)
        
