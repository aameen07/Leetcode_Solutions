class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q=deque()
        q.append(start)
        visited = set()
        visited.add(start)
        
        while q:
            i=q.popleft()
            if arr[i]==0:
                return True
            for j in i+arr[i],i-arr[i]:
                if j>=0 and j<len(arr) and j not in visited:
                    q.append(j)
                    visited.add(j)
        return False