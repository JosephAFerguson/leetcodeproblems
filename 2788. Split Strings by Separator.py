class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = ""
        for i,val in enumerate(words):
            if separator in val:
                replace =words[i].split(separator)
                l = len(replace)
                words.pop(i)
                j = 0
                while j < l:
                    words.insert(i+j, replace[j])
                    j+=1
                i+=l
        
        return [i for i in words if i !=""]
