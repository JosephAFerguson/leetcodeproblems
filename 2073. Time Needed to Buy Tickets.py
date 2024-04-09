class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        n = len(tickets)
        while True:
            for i,val in enumerate(tickets):
                if val> 0:
                    time +=1
                    tickets[i] -=1
                if(tickets[k]) == 0:
                    return time
