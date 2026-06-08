# Lab 5: Classes, Objects, and Feature Branches
#
# Complete the StudentRecord class.


class StudentRecord:
    def __init__(self, name, student_id):
        """
        Create a new student record.

        Parameters:
            name: student name as a string
            student_id: student ID as a string
            scores[]: scores as a list (empty by default)
        """
        self.name = name
        self.student_id = student_id
        self.scores = []


    def add_score(self, score):
        """
        Add one quiz score to this student's list of scores.

        Only add scores between 0 and 100.
        """
        if 0 <= score <= 100:
            self.scores.append(score)

    def calculate_average(self):
        """
        Return the average quiz score.

        If the student has no scores, return None.
        """
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)

    def highest_score(self):
        """
        Return the highest quiz score.

        If the student has no scores, return None.
        """
        if not self.scores:
            return None
        return max(self.scores)

    def lowest_score(self):
        """
        Return the lowest quiz score.

        If the student has no scores, return None.
        """
        if not self.scores:
            return None
        return min(self.scores)

    def letter_grade(self):
        """
        Return a letter grade based on the student's average.

        Suggested scale:
            A: average >= 87
            B: average >= 77
            C: average >= 67
            D: average >= 57
            F: otherwise
        """
        avg = self.calculate_average()
        if avg is None:
            return "N/A"
        if avg >= 87:
            return "A"
        elif avg >= 77:
            return "B"
        elif avg >= 67:
            return "C"
        elif avg >= 57:
            return "D"
        else:
            return "F"

    def __str__(self):
        """
        Return a readable string representation of the student record.
        """
        avg = self.calculate_average()
        avg_str = f"{avg:.2f}" if avg is not None else "No scores"
        grade = self.letter_grade()
        return f"student: {self.name} ({self.student_id}) Average: {avg_str} Grade:{grade}"
