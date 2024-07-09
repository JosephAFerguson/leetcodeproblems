class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        times = []
        time = 0
        for ariv,ti in customers:
            wait = 0
            if time > ariv:
                wait += time-ariv
            else:
                time = ariv
            wait+=ti
            times.append(wait)
            time+=ti
        return sum(times)/len(times)
