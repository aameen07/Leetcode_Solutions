class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=0
        for i in words:
            if set(allowed) >= set(i):
                res+=1
        return res