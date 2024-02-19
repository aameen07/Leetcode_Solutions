class Solution:
    def numUniqueEmails(self, nums: List[str]) -> int:
        d=set()
        for i in nums:
            full=i.split("@")
            last=full[-1]
            front=full[0]
            front=front.split("+")
            front=front[0]
            front=front.replace(".","")
            full=front + "@" +last
            d.add(full)
        return (len(d))
        
        
        