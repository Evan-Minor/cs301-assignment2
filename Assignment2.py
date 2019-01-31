#
# CS301 -Assignment 2
# Lists vs Dictionaries
#
# By David Vandiver, Joshua Swick, Evan Minor
# 
# 

import time


def functionTimer(f, input):
    """
    Returns the approximate runtime of f(input)
    """
    time1 = time.time()
    f(input)
    time2 = time.time()
    return time2 - time1


def graphFunction(f, input_start, input_end, numPoints, output_file_name):
    """
    Writes input, runtimes of f(input) for numPoints 
    to output_file_name.
    """
    file_out = open(output_file_name, "w+")
    input_value = input_start  # Init input
    increment = (input_end-input_start) // numPoints
    for i in range(numPoints):
        runtime = functionTimer(f, input_value)
        file_out.write(f"{str(input_value)},{str(runtime)}\n")
        input_value += increment
    file_out.close()


def func1(data):
	return sum(range(data))


def main():
    # dataSet1 = [x for x in range(10**3)]
    # dataSet2 = [x for x in range(10**6)]
    # dataSet3 = [x for x in range(10**7)]
    # dataSet4 = {x for x in range(10**3)}
    # dataSet5 = {x for x in range(10**4)}
    # dataSet6 = {x for x in range(10**5)}

    graphFunction(func1, 2, 10**6, 10, "graph.csv")


if __name__ == "__main__":
    main()