class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        letters = {}
        l1 = []
        for i in s:
            if i in letters:
                longest = max(longest, len(l1))
                x = letters[i]
                for j in l1[:x]:
                    del letters[j]
                l1 = l1[x+1:]
                l1.append(i)
                for j in range(len(l1)):
                    letters[l1[j]] = j
            else:
                l1.append(i)
                letters[i] = len(l1) - 1
        
        longest = max(longest, len(l1))
        return longest
    
#     A better algorithm
#     class Solution:
#         def lengthOfLongestSubstring(self, s: str) -> int:
#             longest = 0
#             letters = {}
#             left = 0
#             for i in range(len(s)):
#                 if s[i] in letters:
#                     longest = max(i - left, longest)
#                     if letters[s[i]] >= left:
#                         left = letters[s[i]] + 1

#                     letters[s[i]] = i
#                 else:
#                     letters[s[i]] = i

#             longest = max(longest, len(s) - left)
#             return longest
