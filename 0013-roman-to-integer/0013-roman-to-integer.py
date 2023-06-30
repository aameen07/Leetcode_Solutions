class Solution:
    def romanToInt(self, s: str) -> int:
        # roman_dict = {'IV' : 4,
        #               'IX' : 9,
        #               'XL' : 40,
        #               'XC' : 90,
        #               'CD' : 400,
        #               'CM' : 900,
        #               'I' : 1,
        #               "V" : 5,
        #               "X" : 10,
        #               "L" : 50,
        #               "C" : 100,
        #               "D" : 500,
        #               "M" : 1000
        #              }
        # num = 0
        # while (s!=''):
        #     for key in roman_dict :
        #         if key in s :
        #             num += roman_dict[key]
        #             s = s.replace(key,'',1)
        # return num
        
        dic = {'I' : 1,
              "V" : 5,
              "X" : 10,
              "L" : 50,
              "C" : 100,
              "D" : 500,
              "M" : 1000
             }
        n=len(s)
        sum=dic[s[0]]
        for i in range(1,n):
            sum+=dic[s[i]]      
            if dic[s[i-1]] < dic[s[i]]:
                sum-=2*(dic[s[i-1]])
            
        return sum
                
            
            
            
            
            