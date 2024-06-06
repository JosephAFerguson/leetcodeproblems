class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        e1t1 = float(event1[0][:2]) + float(event1[0][3:5])/60
        e1t2 = float(event1[1][:2]) + float(event1[1][3:5])/60
        e2t1 = float(event2[0][:2]) + float(event2[0][3:5])/60
        e2t2 = float(event2[1][:2]) + float(event2[1][3:5])/60

        if e1t1 >= e2t1 and e1t1 <= e2t2:
            return True
        elif e1t2 >= e2t1 and e1t2 <= e2t2:
            return True
        elif e2t1 >= e1t1 and e2t1 <= e1t2:
            return True
        elif e2t2 >= e1t1 and e2t2 <= e1t2:
            return True
        return False
