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
	increment = (end-start)/numPoints
	for i in range(numPoints):
		outputvalue = functionTimer(f, inputvalue)
		f_out.write(str(inputvalue) + " , " + str(outputvalue) + "\n")
		inputValue += increment

def func1(data):
	return data.reverse()

print(functionTimer(func1, dataSet1))
print(functionTimer(func1, dataSet2))
print(functionTimer(func1, dataSet3))