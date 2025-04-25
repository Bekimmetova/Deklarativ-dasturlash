# interval_arithmetic/logic.py

class IntervalLogic:
    def __init__(self, interval):
        self.interval = interval

    def contains(self, value):
        return self.interval.lower <= value <= self.interval.upper

    def equal(self, other_interval):
        return self.interval.lower == other_interval.lower and self.interval.upper == other_interval.upper

    def overlaps(self, other_interval):
        return self.interval.lower <= other_interval.upper and self.interval.upper >= other_interval.lower
