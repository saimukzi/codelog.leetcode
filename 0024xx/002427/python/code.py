from typing import List
import collections
import math

class Solution:

    def commonFactors(self, a: int, b: int) -> int:
        gcd = self.gcd(a,b)
        cnt = self.factor_cnt(gcd)
        return cnt

    def gcd(self, a,b):
        if b < a:
            return self.gcd(b,a)
        if a == b:
            return a
        if a == 0:
            return b
        return self.gcd(a, b%a)

    def factor_cnt(self,x):
        ret = 0
        for i in range(1,x+1):
            if x % i == 0:
                ret += 1
        return ret
