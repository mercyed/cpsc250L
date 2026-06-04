# Lab 4: File I/O and CSV Data Processing
#
# Complete this program so that it reads quiz score data from a CSV file,
# cleans the data, computes student averages, and prints a report.

import csv
def clean_score(score_text):
    """
    Convert a score string into an integer.

    If the score is missing or invalid, return None.
    """
    if score_text == "" or score_text == None:
        return None
    if score_text.isdigit():
        return int(score_text)
    else:
        return None


def calculate_average(scores):
    """
    Calculate the average of a list of numeric scores.

    If the list is empty, return None.
    """
    sum = 0
    count = 0
    for score in scores:
        if score is not None:
            sum += score
            count += 1
    if count > 0:
        return sum / count
    else:
        return None


def read_scores(filename):
    """
    Read student quiz scores from a CSV file.

    Return a list of dictionaries.

    Each dictionary should contain:
        "name": student name
        "scores": list of valid numeric quiz scores
        "average": student average

    So, the returned list of dictionaries should look like:
    [
        {
            "name": "Alice",
            "scores": [85, 90, 78],
            "average": 84.33
        },
        {
            "name": "Bob",
            "scores": [92, None, 88],
            "average": 90.0
        },
        ...
    ]
    """
    my_list = []
    #open file and read it with csv reader
    with open(filename) as csvfile:
       reader = csv.reader(csvfile)
       for row in reader:
           # ignore first row
        if reader.line_num == 1:
            continue
        else:
            # convert this line into a dict
            name = row[0]
            scores = [clean_score(row[1]),clean_scores(row[2]),clean_score(row[3])]
            average = calculate_average(scores)
            my_dict = {"name":  name, "scores": scores_list, "average": avgerage}
            my_list.append(my_dict)
    return my_list

def letter_grade(average):
    """
    Return a simple letter grade based on the average.

    Suggested scale:
        A: average >= 87
        B: average >= 77
        C: average >= 67
        D: average >= 57
        F: otherwise

    If the average is None, return "N/A".
    """
    # if there is no avarege we cannont grade
if average == None:
    return "N/A"
   #check for range higest to lowest
if average >= 87:
    return "A"
elif average >= 77:
    return "C"
elif average >= 57:
    return "D"
else:
    return "F"


def print_student_report(records):
    """
    Print one line of output for each student.
    """



def print_class_summary(records):
    """
    Print a summary for the whole class.

    Include:
        number of students
        class average
        highest average
        lowest average
    """
    pass


def main():
    filename = "../data/quiz_scores.csv"
    #
    records = read_scores(filename)

    print_student_report(records)
    print()
    print_class_summary(records)


main()
