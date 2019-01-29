import time

dataSet1 = [x for x in range(10**3)]
dataSet2 = [x for x in range(10**6)]
dataSet3 = [x for x in range(10**7)]
dataSet4 = {x for x in range(10**3)}
dataSet5 = {x for x in range(10**4)}
dataSet6 = {x for x in range(10**5)}

def functionTimer(f, input):
	time1 = time.time()
	f(input)
	time2 = time.time()
	return time2 - time1

def graphFunction(f, start, end, numPoints, file):
	f_out = open(file, "w+")
	inputvalue = start
	increment = (end-start)//numPoints
	for i in range(numPoints):
		outputvalue = functionTimer(f, inputvalue)
		f_out.write(str(inputvalue) + " , " + str(outputvalue) + "\n")
		inputvalue += increment
	f_out.close()

def func1(data):
	return sum(range(data))

graphFunction(func1, 2, 10**6, 10, "graph.csv")