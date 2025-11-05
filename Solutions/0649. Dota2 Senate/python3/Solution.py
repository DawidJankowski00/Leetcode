from collections import Counter, deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr = deque()
        qd = deque()
        for i, v in enumerate(senate):
            if v == "R":
                qr.append(i)
            else:
                qd.append(i)
        n = len(senate)
        while qr and qd:
            player_R = qr.popleft()
            player_D = qd.popleft()
            if player_R < player_D:
                qr.append(n)
            else:
                qd.append(n)
            n += 1
        if qr:
            return "Radiant"
        else:
            return "Dire"