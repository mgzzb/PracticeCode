class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # find the letters in string
        letters = set(s)

        # count palindromes found
        final = 0

        for l in letters:
            i, j = s.index(l), s.rindex(l)
            palindrome = set()

            # iterate over letters inside indexes found
            for k in range(i + 1, j):
                palindrome.add(s[k]) # only add once a letter
            
            final += len(palindrome)

        # return count of palindromes found
        return final

       # one line
       # return sum([len(set(s[s.index(l)+1:s.rindex(l)])) for l in set(s)]) 
