def read_temperatures(filename):
   # read temps from file
   temperatures = []

with open(read_temperatures(), 'r') as file:
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
    pass

def print_report(values):
    pass

def main():
    temperatures = read_temperatures("../data/june_temperatures.txt")
    print_report(temperatures)

main()
