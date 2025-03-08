class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        j  = k
        maxb = 0
        currb = 0
        while i < j:
            if(blocks[i]=="B"):
                currb +=1
            i+=1
        i = 0
        maxb = max(maxb,currb)#edgecase
        while j < len(blocks):
            maxb = max(maxb,currb)
            if blocks[j] == "B":
                currb +=1
            if blocks[i] == "B":
                currb -=1
            i+=1
            j+=1
        maxb = max(maxb,currb)#edgecase
        if (k-maxb) <= 0:
            return 0
        return k-maxb
