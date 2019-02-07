#
# CS301 -Assignment 2
# Lists vs Dictionaries
#
# By David Vandiver, Joshua Swick, Evan Minor
# 
# 

import time
import os

#
#   Comparison functions and output data to csv
#

def functionTimer(f, input):
    """
    Returns the approximate runtime of f(input)
    """
    time1 = time.time()
    f(input)
    time2 = time.time()
    return time2 - time1


def graphFunction_List(f, input_start, input_end, numPoints, output_file_name):
    """
    Writes input, runtimes of f(input) for numPoints 
    to output_file_name.
    """
    file_out = open(output_file_name, "w+")
    input_value = input_start  # Init input
    increment = (input_end-input_start) // numPoints
    for i in range(numPoints):
        dataList = listConverter(input_value)
        runtime = functionTimer(f, dataList)
        file_out.write(f"{str(len(dataList))},{str(runtime)}\n")
        input_value += increment
    file_out.close()


def graphFunction_Dictionary(f, input_start, input_end, numPoints, output_file_name):
    file_out = open(output_file_name, "w+")
    input_value = input_start  # Init input
    increment = (input_end-input_start) // numPoints
    for i in range(numPoints):
        data_dict = createDictionary("words.txt",input_value)
        runtime = functionTimer(f, data_dict)
        file_out.write(f"{str(len(data_dict))},{str(runtime)}\n")
        input_value += increment
    file_out.close()


#
#   Create data structures
#

def listConverter(amount):
    values = []
    times = 0
    with open("words.txt") as fi:
        for line in fi:
            if times > amount:
                return values
            else:
                values.append(line.strip())
                times += 1


def createDictionary(fileName,numItems):
    #Create counter variable and initiate dictionary
    dictionary = {}
    count = 0
    #open the file and read lines
    with open(fileName) as f:
        words = f.read().splitlines()
    #creat a loop that adds to the dictionary 
    for i in words:
        dictionary[count] = i
        count +=1
        #check to see if you have reached your number of items
        if  count == numItems:
            break
    #return the dictionary
    return dictionary


#
#   Things to do to a list
#

def appendFoo_list(data):
    """
    Adds 'foo' to the end of the given list.
    """
    return data.append("foo")


def sort_list(data):
    """
    Returns a sorted version of the given list.
    """
    return data.sort()


def concatentateFooToEachElement_list(data):
    """
    Adds 'foo' the each element in the given list. The element must be a string.
    """
    return [l + "foo" for l in data]


def getFirstElement_list(data):
    """
    Returns first element of the list.
    """
    return data[0]


def countNumOfElements_list(data):
    """
    Returns the number of elements in the list or dictionary.
    """
    numOfElements = 0
    for element in data:
        numOfElements += 1
    return numOfElements


def lengthOf_list(data):
    """
    Returns the length of the given list.
    """
    return len(data)

def getLastElement_list(data):
    """
    Returns the last element of the list.
    """
    return data[-1]

def reverse_list(mylist):
    """
    Reverses the list
    """
    return mylist.reverse()

#
#   Things to do to a dictionary
#

def appendFoo_dict(data):
    """
    Adds 'foo' to dict.
    """
    data[len(data)] = "foo"
    return True


def sort_dict(data):
    """
    Dictionaries are insertion ordered as of Python 3.7, they cannot be sorted.
    """
    return False


def concatentateFooToEachElement_dict(data):
    """
    Adds 'foo' to each element in the given dictionary. The element must be a string.
    """
    for index in data:
        data[index] = data[index] + "foo"
    return True


def getFirstElement_dict(data):
    """
    Gets first element from the given dictionary.
    """
    return data[0]


def countNumOfElements_dict(data):
    """
    Counts the number of Elements in a dictionary.
    """
    numElements = 0
    for element in data:
        numElements += 1
    return numElements


def lengthOf_dict(data):
    """
    Returns the length of a dictionary.
    """
    return len(data)


def getLastElement_dict(data):
    """
    Returns the last element of a dictionary.
    """
    last_key = list(data.keys())[-1]
    return data[last_key]
    

def main(number_of_elements=100000):

    # List and Dict preparation
    file_name = "words.txt"
    if not os.path.exists("csvs/"):
        os.mkdirs("csvs/")

    # # Create List from file
    # list_data_structure = listConverter(number_of_elements)

    # # Create dict from file
    # dict_data_structure = createDictionary(file_name,number_of_elements)

    # Get graph data for different functions
    graphFunction_List(appendFoo_list, 1, number_of_elements, 15, "csvs/appendFoo_list.csv")
    graphFunction_Dictionary(appendFoo_dict, 1, number_of_elements, 15, "csvs/appendFoo_dict.csv")

    graphFunction_List(sort_list, 1, number_of_elements, 15, "csvs/sort_list.csv")
    graphFunction_Dictionary(sort_dict, 1, number_of_elements, 15, "csvs/sort_dict.csv")

    graphFunction_List(concatentateFooToEachElement_list, 1, number_of_elements, 15, "csvs/concatenateFooToEachElement_list.csv")
    graphFunction_Dictionary(concatentateFooToEachElement_dict, 1, number_of_elements, 15, "csvs/concatenateFooToEachElement_dict.csv")

    graphFunction_List(getFirstElement_list, 1, number_of_elements, 15, "csvs/getFirstElement_list.csv")
    graphFunction_Dictionary(getFirstElement_dict, 1, number_of_elements, 15, "csvs/getFirstElement_dict.csv")

    graphFunction_List(countNumOfElements_list, 1, number_of_elements, 15, "csvs/countNumOfElements_list.csv")
    graphFunction_Dictionary(countNumOfElements_dict, 1, number_of_elements, 15, "csvs/countNumOfElements_dict.csv")

    graphFunction_List(lengthOf_list, 1, number_of_elements, 15, "csvs/lengthOf_list.csv")
    graphFunction_Dictionary(lengthOf_dict, 1, number_of_elements, 15, "csvs/lengthOf_dict.csv")

    graphFunction_List(getLastElement_list, 1, number_of_elements, 15, "csvs/getLastElement_list.csv")
    graphFunction_Dictionary(getLastElement_dict, 1, number_of_elements, 15, "csvs/getLastElement_dict.csv")
    

if __name__ == "__main__":
    main()
