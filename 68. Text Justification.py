class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        lineL = []
        curr = 0
        currL = []
        """
            len(words)-1 = number of spaces a sentence will have normally without justifications
        """
        #got through words, find maximum amount of words to fit in a line, and then append that list of
        #words to a list to be later justified
        for i in words:
            if len(i) + curr + len(currL)-1 >= maxWidth:
                lines.append(currL)
                lineL.append(curr+len(currL)-1)
                curr = len(i)
                currL = [i]
            else:
                curr+=len(i)
                currL.append(i)
        #edge case where the last element added goes over maxwidth
        if len(i) + curr + len(currL)-1 > maxWidth:
                lines.append(currL)
                lineL.append(curr+len(currL)-1)
                curr = len(i)
                currL = [i]
        else:
            lines.append(currL)
            lineL.append(curr+len(currL)-1)

        #go thrugh each line except last and justify it
        for i,line in enumerate(lines):
            togo = maxWidth - lineL[i] + (len(line)-1)
            if len(line) > 1 and i!=len(lines)-1:
                #fill in spaces one by one, left to right until we reach maxWidth
                j = 1 # start at second element and add space beforehand
                while togo>0:
                    if j >= len(line):
                        j = 1
                    line[j] = " " + line[j]
                    togo-=1
                    j+=1
            elif len(line) ==1: # works even if last line since single word is left-justified anyway
                line[0] = line[0] + " "*togo
        
        res = []
        #python join the lines into strings/sentences except the last one which is specially left justified
        for i in range(len(lines)-1):
            res.append("".join(lines[i]))
        #edge case handled if last line is single word
        if len(lines[-1])>1:
            space = maxWidth - lineL[-1] 
            res.append(" ".join(lines[-1]) + " "*space)
        else:
            res.append("".join(lines[-1]))
        return res
        
