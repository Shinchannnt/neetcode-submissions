class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w1= 0 #word pointer
        a1= 0 #abb pointer
       
        while (a1<=len(abbr)-1 and w1<=len(word)-1):
           
            if word[w1]==abbr[a1]:
                w1+=1
                a1+=1
            
            elif abbr[a1].isdigit():
                    if abbr[a1] == '0':  # Leading zeros are invalid in abbreviations
                        return False
                    if a1+1<len(abbr) and abbr[a1+1].isdigit() :
                        skip=int(abbr[a1]+abbr[a1+1])
                        a1=a1+2
                    else:
                        skip=int(abbr[a1])
                        a1=a1+1
                
                    w1=w1+skip
                   
            elif abbr[a1]!=word[w1]:
                return False
        if w1==len(word) and a1==len(abbr):
            return True
        else:
            return False




