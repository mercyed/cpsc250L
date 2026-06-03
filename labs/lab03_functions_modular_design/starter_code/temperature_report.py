def read_temperatures(filename):
   # read temps from file
    temperatures = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                temperatures.append(float(line))
    return temperatures
# open files and check for blank lines then returns the float of the temps

def calculate_average(values):
    if not values:
        return 0.0
    return sum(values) / len(values)
# computes average
def find_maximum(values):
    if not values:
        return None
    return max(values)
# finds max and returns the max values
def find_minimum(values):
    if not values:
        return None
    return min(values)
# finds min and checks if it is avaiable

def count_above_threshold(values, threshold):
    return sum(1 for t in values if t > threshold)
# counts above threshold and checks if it is above it

def print_report(values):
    if not values:
        print("No temperature data avaiable")
        return
    # computetes stats and prints report values
    avg_temp = calculate_average(values)
    max_temp = find_maximum(values)
    min_temp = find_minimum(values)
    above_80 = count_above_threshold(values, 80)

    print("Temperature Report")
    print("------------------")
    print(f"Average temperature: {avg_temp:.1f}")
    print(f"Maximum temperature: {int(max_temp)if max_temp.is_integer()else max_temp}")
    print(f"Minimum temperature: {int(min_temp)if min_temp.is_integer() else min_temp}")
    print(f"Temperatures above 80: {above_80}")
    # prints the values and checks if it is above 80 and will check if the min and max temps are integers or not.
def main():
    temperatures = read_temperatures("../data/june_temperatures.txt")
    print_report(temperatures)

main()
