class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        res=[]
        rows = len(img)
        cols = len(img[0])
        
        for r, row in enumerate(img):
            res.append([])
            for c,col in enumerate(row):
                s=0
                count=0
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if r+dx>=0 and r+dx<rows and c+dy<cols and c+dy>=0:
                            s+=img[dx+r][dy+c]
                            count+=1
                res[-1].append (s//count)
        return res