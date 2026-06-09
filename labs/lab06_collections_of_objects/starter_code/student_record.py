# Lab 6: Collections of Objects

class StudentRecord:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average(self):
        valid_scores = []

        for score in self.scores:
            if score is not None:
                valid_scores.append(score)

        if len(valid_scores) == 0:
            return None

        return sum(valid_scores) / len(valid_scores)

    def highest_score(self):
        valid_scores = []

        for score in self.scores:
            if score is not None:
                valid_scores.append(score)

        if len(valid_scores) == 0:
            return None

        return max(valid_scores)

    def lowest_score(self):
        valid_scores = []

        for score in self.scores:
            if score is not None:
                valid_scores.append(score)

        if len(valid_scores) == 0:
            return None

        return min(valid_scores)

    def letter_grade(self):
        average = self.calculate_average()

        if average is None:
            return "N/A"
        elif average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return (
            f"StudentRecord(name={self.name}, "
            f"student_id={self.student_id}, "
            f"scores={self.scores})"
        )