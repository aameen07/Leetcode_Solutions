class Solution:
    def numUniqueEmails(self, nums: List[str]) -> int:
        l=set()
        for i in nums:
            full=i.split("@")
            domain=full[-1]
            local=full[0]
            local=local.split("+")
            local=local[0]
            local=local.replace(".","")
            full=local + "@" + domain
            
            l.add(full)
        
        return (len(l))
        