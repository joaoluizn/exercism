class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return sorted(self.scores)[-1]

    def personal_top_three(self):
        if len(self.scores) < 3:
            return sorted(self.scores, reverse=True)
        else:
            return sorted(self.scores, reverse=True)[:3]
