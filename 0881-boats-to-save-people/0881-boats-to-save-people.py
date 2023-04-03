class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        l=0
        r=len(people)-1
        c=0        
        while(l<=r):
            if people[l]+people[r]<=limit:
                l+=1
                r-=1
            else:
                r-=1
            c+=1
        return c
    
    # or
    
        # people.sort(reverse=True)
        # print(people)
        # i, j = 0, len(people) - 1
        # print(i,j)
        # while i <= j:
        #     if people[i] + people[j] <= limit: j -= 1
        #     i += 1
        #     print(i,j)
        # return i