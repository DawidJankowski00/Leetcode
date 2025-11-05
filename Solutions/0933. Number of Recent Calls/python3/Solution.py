class RecentCounter:
    def __init__(self):
        self.records = []
        self.k = 0

    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[self.k] < t - 3000:
            self.k += 1
        return len(self.records) - self.k