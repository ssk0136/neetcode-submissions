import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for i in s:
            if i.isalnum():
                st+=i.lower()

        for x in range(len(st)//2):
            if st[x]!=st[len(st)-x-1]:
                return False
        return True