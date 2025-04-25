# interval_arithmetic/ai_system.py

import numpy as np
from .arithmetic import Interval

class IntervalAI:
    def __init__(self, interval_data):
        self.interval_data = interval_data

    def analyze(self):
        # Bu yerda intervalni sun'iy intellekt tizimi uchun tahlil qilish
        intervals = [Interval(lower, upper) for lower, upper in self.interval_data]
        results = [interval.upper - interval.lower for interval in intervals]
        return np.mean(results), np.std(results)

    def make_decision(self):
        mean, std = self.analyze()
        if mean > 5:
            return "Qaror: O'rtacha interval kattaligi katta"
        else:
            return "Qaror: O'rtacha interval kattaligi kichik"
