#
# CS301 -Assignment 2
# Lists vs Dictionaries
#
# By David Vandiver, Joshua Swick, Evan Minor
# 
# 

import time


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
    dictionary = []
    count = 0
    #open the file and read lines
    with open(fileName) as f:
        words = f.read().splitlines()
    #creat a loop that adds to the dictionary 
    for i in words:
        temp ={count: i}
        dictionary.append(temp)
        count +=1
        #check to see if you have reached your number of items
        if  count == numItems:
            break
    #return the dictionary
    return dictionary


#
#   Things to do to list
#

def listFunc1(data):
    return data.append("foo")

def listFunc2(data):
    return data.sort()

def listFunc3(data):
    return [l + "foo" for l in data]


def getFirstElement(data):
    """
    Returns first element of the list or dictionary.
    """
    return data[0]


def numOfElements(data):
    """
    Returns the number of elements in the list or dictionary.
    """
    numOfElements = 0
    for element in data:
        numOfElements += 1
    return numOfElements

#
#   Things to do to dictionaries
#

def dictFunc1(data):
    pass




def main():

    # List and Dict preparation
    file_name = "words.txt"
    length_of_list = 100000

    # Create List from file
    print("Creating list...")
    list_data_structure = listConverter(length_of_list)
    #print(list_data_structure)

    # Create dict from file
    print("Creating dictionary")
    dict_data_structure = createDictionary(file_name,length_of_list)
    #print(dict_data_structure)

    # Get graph data for different functions
    graphFunction_List(listFunc1, 1, 1000, 15, "listFunc1.csv")
    graphFunction_Dictionary(listFunc1, 1, 1000, 15, "dictFunc1.csv")
    

if __name__ == "__main__":
    main()
