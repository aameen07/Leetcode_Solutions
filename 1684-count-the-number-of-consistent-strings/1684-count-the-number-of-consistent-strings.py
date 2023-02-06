class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=0
        a = set(allowed)
        for i in words:
            if a >= set(i):
                res+=1
        return res