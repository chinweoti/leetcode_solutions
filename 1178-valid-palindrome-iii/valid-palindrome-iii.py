class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # queue holds a tuple of `l` and `r`, and the depth `curr_k`.
        queue = deque([(0, len(s) - 1, 0)])
        visited = [[False for j in range(len(s))] for i in range(len(s))]
    
        while queue:
            l, r, curr_k = queue.popleft()

            # If the budget is exceeded return False
            if curr_k > k:
                return False

            # Shave off the two ends of s[l:r+1] until end characters 
            # don't match. Each graph node is defined by (l,r)
            # where s[l] != s[r].
            while s[l] == s[r]:
                l += 1
                r -= 1
                # if you reach the end node, you've found a k-palindrome
                if l >= r:
                    return True

            # append the two new nodes to the queue.
            if not visited[l+1][r]:
                queue.append((l+1, r, curr_k+1))
                visited[l+1][r] = True

            if not visited[l][r-1]:
                queue.append((l, r-1, curr_k+1))
                visited[l][r-1] = True


# l = 0 
#         r = len(s)-1
#         sl = s

#         while l < r:
#             if sl[l] == sl[r]:
#                 l += 1
#                 r -= 1
#             elif  sl[l] != sl[r]:
#                 if sl[l+1] == sl[r] and k > 0:
#                     l +=1
#                     k -= 1
#                 elif sl[r-1] == sl[l] and k > 0:
#                     r -=1
#                     k -=1 
#                 else:
#                     if k == 0:
#                         return False
#             else: 
#                 if sl[l] != sl[r]:
#                     return False
#         return True
            

