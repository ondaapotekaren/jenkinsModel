import numpy

#curList = [0] * executors

#accList = [0] * executors

#queue = [1,3,4,5,6,5,9,4,5,2,3]

s =  (numpy.random.pareto(2,100) + 1)

queue = []

for i in s:
	queue.append(int(i*100))

print("The queue: " + str(queue)+'\n') 
print("max entry in queue: " + str(max(queue))+'\n')

nodes = 2
nodeList = []
executors = 10


# (currently running,accumulated time)

for i in range(nodes):
	nodeList.append(([0]*executors,[0]*executors))

while len(queue) > 0:


	freeSlots = False
	for i in range(len(nodeList)):
		for ii in range(len(nodeList[i][0])):
			if nodeList[i][0][ii] == 0:
				freeSlots = True

	if(freeSlots):

		# add from queue	

		curNode = 0
		highestScore = 0
			
		# load balancer
		# find node
		for i in range(len(nodeList)):
			# calc score
			busy = 0
			for ii in range(len(nodeList[i][0])):
				if nodeList[i][0][ii] != 0:
					busy = busy + 1
			score = float(len(nodeList[i][0]))/(float(busy)+0.5) 
			if  score > highestScore:
				highestScore = score
				curNode = i

		# add job from queue to a node,first available executor

		temp = int(queue.pop(0))
		for i in range(len(nodeList[curNode][0])):
			if nodeList[curNode][0][i] == 0:
				nodeList[curNode][0][i] = temp
				nodeList[curNode][1][i] += temp
				break

		
	else:

	# if there are no free slots 
	# subtract one time unit from all executors

		for i in range(len(nodeList)):
			for ii in range(len(nodeList[i][0])):
					nodeList[i][0][ii] -= 1


print(nodeList)

curMax = 0
for i in nodeList:
	x = max(i[1])
	if x > curMax:
		curMax = x

print("Makespan: "+str(curMax))