class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mos=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        d = dict(zip("abcdefghijklmnopqrstuvwxyz",mos))
        
        res=[]
        for i in words:
            a=""
            for letter in i:
                a+="".join(d[letter])
            res.append(a)
        return (len(set(res)))
            