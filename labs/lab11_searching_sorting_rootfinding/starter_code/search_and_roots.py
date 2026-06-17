def linear_search(values, target):
    compare = 0

    for i in range(len(values)):
        compare += 1
        if values[1] == target:
            return i, compare

    return -1, compare



def binary_search(values, target):
    left = 0
    right = len(values) - 1
    compare = 0

    while left <= right:
        mid = (left + right) // 2
        compare += 1

        if values[mid] == target:
            return mid, compare
        elif values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, compare


def f(x):
    return x * x - 2


def bisection_root(function, left, right, tolerance):
    pass


def main():
    import random
    values = random.sample(range(0, 1000), 500)
    values.sort()

    # Find the 500th value in the list
    search_value = values[249]

    print("Search Tests")
    print("------------")
    print("Linear search for ", search_value," --> (index,comps) = ", linear_search(values, search_value))
    print("Binary search for ", search_value," --> (index,comps) = ", binary_search(values, search_value))

    print()
    print("Root Finding")
    print("------------")
    root = bisection_root(f, 1, 2, 0.0001)
    print("Approximate root of x^2 - 2:", root)

main()
