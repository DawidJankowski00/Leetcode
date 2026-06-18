class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = 6 * minutes
        b = minutes * 0.5
        if hour != 12:
            b += 30 * hour
        tmp = abs(a - b)
        if tmp > 180:
            return 360 - tmp
        return tmp