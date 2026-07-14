class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x=abs(x)
        Max_Val=2**31-1
        Min_Val=-2**31
        rev=0
        while x != 0:
            r=x%10
            rev=rev*10+r
            x//=10
        rev*=sign
        if rev <= Min_Val or rev >= Max_Val:
            return 0

        return rev    