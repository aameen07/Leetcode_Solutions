class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic={}
        
        for i in strs:
            sorted_str = "".join(sorted(i))
            
            if sorted_str not in dic:
                dic[sorted_str] = []
            
            dic[sorted_str].append(i)
            
        return list(dic.values())
    

# We simply used the idea of sorted string this helped in finding the commonality in the anagrams. Then we simply stacked them under that sorted string key in a list and in the end returned all the values together in list format. 