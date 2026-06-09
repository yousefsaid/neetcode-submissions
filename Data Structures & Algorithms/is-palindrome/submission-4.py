class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitizedS =  s.lower()
        L = 0
        R = len(sanitizedS) - 1

        while L < R:
            

            while L < R and not sanitizedS[L].isalnum():
                L += 1
            
            while L < R and not sanitizedS[R].isalnum():
                R -= 1
            
            if sanitizedS[L] == sanitizedS[R]:
                L += 1
                R -= 1
            else:
                return False
        return True


            