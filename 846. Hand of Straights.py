class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        
        if n % groupSize != 0:
            return False
        sublen = n / groupSize
        arr = []
        hand = sorted(hand)
        while len(arr) < sublen:
            i = 0
            j = 0
            sub = []
            while i < groupSize:
                if i == 0:
                    sub.append(hand[0])
                    hand.pop(0)
                else:
                    n = len(hand)
                    while j<n and hand[j] != sub[-1]+1:
                        j+=1
                    if j==n:
                        return False
                    sub.append(hand[j])
                    hand.pop(j)
                i+=1
            arr.append(sub)
        return True

        
