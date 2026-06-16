import time
import matplotlib.pyplot as plt


def fib_recursive(n):
    # TODO: write this function
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n):
    # TODO: write this function
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def time_function(function, n):
    # TODO: write this function - google the python time module to figure out how it works
    # TODO: start a timer, call the appropriate function, then stop the timer
    # TODO: return the elapsed time
    start_time = time.perf_counter()

    function(n)

    end_time = time.perf_counter()

    return end_time - start_time

def main():
    values = [5, 10, 20, 25, 30, 35, 40]

    print("Fibonacci Timing")
    print("----------------")
    print("n    recursive_time    iterative_time         speed_factor")
    hi = []
    bye = []
    for n in values:
        recursive_time = time_function(fib_recursive, n)
        iterative_time = time_function(fib_iterative, n)
        hi.append(recursive_time)
        bye.append(iterative_time)
        if iterative_time != 0:
            speed = recursive_time/iterative_time
        else:
            speed = float("inf")
        print(f"{n:<5} {recursive_time:.8f} seconds    {iterative_time:.8f} seconds     {speed:.1f}")

    # TODO: create a plot which shows both recursive time and iterative time as a function of n
    # TODO: label the x-axis, y-axis, and provide a title
    # TODO: display a legend that will indicate which dataset is which
    # TODO: make the y-axis logarithmic

    plt.plot(values, hi, marker="o", label="Recursive")
    plt.plot(values, bye, marker="o", label="Iterative")

    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Fibonacci Timing")
    plt.yscale("log")
    plt.legend()

    plt.show()

main()
