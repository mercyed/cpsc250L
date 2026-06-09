# Lab 6: Collections of Objects

from student_record import StudentRecord


def clean_score(score_text):
    """
    Convert score text to an integer.
    Return None if the score is missing or invalid.
    """
    score_text = score_text.strip()

    if score_text == "":
        return None

    if not score_text.isdigit():
        return None

    score = int(score_text)

    if score < 0 or score > 100:
        return None

    return score


def read_student_records(filename):
    """
    Read the CSV file and return a list of StudentRecord objects.
    """
    students = []

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines[1:]:
        parts = line.strip().split(",")

        name = parts[0]
        student_id = parts[1]

        student = StudentRecord(name, student_id)

        for score_text in parts[2:]:
            student.add_score(clean_score(score_text))

        students.append(student)

    return students


def class_average(students):
    """
    Return the average of all student averages.
    Ignore students with no valid scores.
    """
    averages = []

    for student in students:
        average = student.calculate_average()

        if average is not None:
            averages.append(average)

    if len(averages) == 0:
        return 0

    return sum(averages) / len(averages)


def find_highest_average_student(students):
    """
    Return the StudentRecord object with the highest average.
    """
    highest_student = None
    highest_average = -1

    for student in students:
        average = student.calculate_average()

        if average is not None and average > highest_average:
            highest_average = average
            highest_student = student

    return highest_student


def find_lowest_average_student(students):
    """
    Return the StudentRecord object with the lowest average.
    """
    lowest_student = None
    lowest_average = float("inf")

    for student in students:
        average = student.calculate_average()

        if average is not None and average < lowest_average:
            lowest_average = average
            lowest_student = student

    return lowest_student


def print_class_report(students):
    """
    Print all student records and a class summary.
    """
    for student in students:
        print(student)

    print(f"\nClass average: {class_average(students):.2f}")

    highest_student = find_highest_average_student(students)

    if highest_student is not None:
        print(
            f"Highest average: {highest_student.name} "
            f"with {highest_student.calculate_average():.2f}"
        )

    lowest_student = find_lowest_average_student(students)

    if lowest_student is not None:
        print(
            f"Lowest average: {lowest_student.name} "
            f"with {lowest_student.calculate_average():.2f}"
        )


def main():
    students = read_student_records("../data/student_scores.csv")
    print_class_report(students)


main()