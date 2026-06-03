def read_temperatures(filename):
   # read temps from file
    filename =  temperatures = []

with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
    if line:
        temperatures.append(float(line))

print(read_temperatures())


def calculate_average(values):
    if not values:
        return 0.0
    return sum(values) / len(values)
# computes average
def find_maximum(values):
    if not values:
        return None
    return max(values)
# finds max
def find_minimum(values):
    if not values:
        return None
    return min(values)
# finds min

def count_above_threshold(values, threshold):
    return sum(1 for t in values if t > threshold)
# counts above threshold

def print_report(values):
    pass

def main():
    temperatures = read_temperatures("../data/june_temperatures.txt")
    print_report(temperatures)

main()
