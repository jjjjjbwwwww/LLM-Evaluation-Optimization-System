

# app/evaluator/metrics.py

class Metrics:

    def __init__(self):
        self.records = []

    def add(self, score):
        self.records.append(score)

    def summary(self):
        if not self.records:
            return {}

        avg = {}
        keys = self.records[0].keys()

        for k in keys:
            avg[k] = sum(r[k] for r in self.records) / len(self.records)

        return avg