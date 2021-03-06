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
        dataList = listConverter(input_value)
        runtime = functionTimer(f, dataList)
        file_out.write(f"{str(input_value)},{str(runtime)}\n")
        input_value += increment
    file_out.close()

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

def createDictionary(fileName,numItems):
    #Create counter variable and initiate dictionary
    dictionary = {}
    count = 0
    #open the file and read lines
    with open(fileName) as f:
        words = f.read().splitlines()
    #creat a loop that adds to the dictionary 
    for i in words:
        #temp ={count: i}
        dictionary[count] = i
        count +=1
        #check to see if you have reached your number of items
        if  count == numItems:
            break
    #return the dictionary
    return dictionary

def testTimeFunction(f1, input1, input11, f2, input2, input22):
    #Function 1 times
    startf1 = time.time()
    f1(input1)
    endf1 = time.time()
    #Function 2 times
    startf2 = time.time()
    f2(input2, input22)
    endf2 = time.time()
    #total times
    totaltimef1 = endf1-startf1
    totaltimef2 = endf2-startf2
    #compare total times
    finalTimes = {f1:totaltimef1, f2: totaltimef2}
    return finalTimes

def main():
    # dataSet1 = []
    # dataSet2 = []
    # dataSet3 = []
    # dataSet4 = {x for x in range(10**3)}
    # dataSet5 = {x for x in range(10**4)}
    # dataSet6 = {x for x in range(10**5)}

    graphFunction(listFunc1, 1, 1000, 10, "graph.csv")
    graphFunction(listFunc2, 1, 113809, 15, "graph1.csv")
    graphFunction(listFunc3, 1, 113809, 15, "graph2.csv")

if __name__ == "__main__":
    main()
