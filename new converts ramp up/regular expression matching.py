class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dp(i, j):
            if (i, j) not in memoization:
                if j == len(p):
                    ans =  i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}

                    if j < len(p) - 1 and p[j + 1] == '*':
                        ans =  (dp(i, j + 2) or
                                first_match and dp(i + 1, j))
                    else:
                        ans =  first_match and dp(i + 1, j + 1)
                
                memoization[(i, j)] = ans
            
            return memoization[(i, j)]
        
        memoization = {}
        return dp(0, 0)
