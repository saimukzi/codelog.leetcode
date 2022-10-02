from typing import List
import collections
import math
import sys

SMALL_PRIME = 211
BIG_PRIME = 1000003

class Solution:
    def deleteString(self, s: str) -> int:
        sys.setrecursionlimit(10000) # cheat
        dfs_ans_list = [None] * len(s)
        return self.dfs(s,0,dfs_ans_list)

    def dfs(self, s, i, dfs_ans_list):
        if dfs_ans_list[i] != None:
            return dfs_ans_list[i]
        
        ret = self._dfs(s,i,dfs_ans_list)
        dfs_ans_list[i] = ret
        
        return ret

    def _dfs(self, s, i, dfs_ans_list):
        s_len = len(s)
        
        if i == s_len: return 0
        if i == s_len-1: return 1
        
        ret = 1
        
        ii = i
        jj = i+1
        kk = i+2
        s0 = ord(s[ii])
        s1 = ord(s[jj])
        
        if (dfs_ans_list[jj] == None) or (dfs_ans_list[jj] + 1 > ret):
            if s0 == s1:
                if s[ii:jj] == s[jj:kk]:
                    ret = max(ret, self.dfs(s,jj,dfs_ans_list)+1)
        
        pp = 1
        while True:
            s0 *= SMALL_PRIME
            s0 += ord(s[jj])
            s1 -= ord(s[jj]) * pp
            jj += 1
            if kk >= s_len: break
            s1 *= SMALL_PRIME
            s1 += ord(s[kk])
            kk += 1
            if kk >= s_len: break
            s1 *= SMALL_PRIME
            s1 += ord(s[kk])
            kk += 1
            
            s0 += 1000003 * 211
            s0 %= BIG_PRIME
            s1 += 1000003 * 211
            s1 %= BIG_PRIME
            pp *= SMALL_PRIME
            pp %= BIG_PRIME

            if (dfs_ans_list[jj] == None) or (dfs_ans_list[jj] + 1 > ret):
                if s0 == s1:
                    #if s[ii:jj] == s[jj:kk]:
                    ret = max(ret, self.dfs(s,jj,dfs_ans_list)+1)
        
        return ret
