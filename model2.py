import numpy
import sys

#curList = [0] * executors

#accList = [0] * executors

queue = [2,2,2,2,1,1,1,1,1]

## LJF, SJF. Just sort the queue asc or des

## To add aging: Split the queue sort them separately, then join them.


nmbrOfTests = int(sys.argv[1])

makespan = 0

for x in range(nmbrOfTests):

	s =  (numpy.random.pareto(2,100) + 1)

	queue = []

	for i in s:
		queue.append(int(i*100))

	#print("The queue: " + str(queue)+'\n') 
	#print("max entry in queue: " + str(max(queue))+'\n')

	nodes = 2
	nodeList = []
	executors = 2


	# (currently running,accumulated time)

	for i in range(nodes):
		nodeList.append(([0]*executors,[[] for _ in range(executors)]))

	while len(queue) > 0:


		freeSlots = False
		for i in range(len(nodeList)):
			for ii in range(len(nodeList[i][0])):
				if nodeList[i][0][ii] == 0:
					freeSlots = True
					break
			if freeSlots:
				break

		if freeSlots:

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
					#nodeList[curNode][1][i] += temp

					if temp > 300:  
						job = (temp,True)

					else:
						job = (temp,False)

					nodeList[curNode][1][i].append(job)
					#print("break with job: " + str(temp))
					break

			
		else:

		# if there are no free slots 
		# subtract one time unit from all executors

			for i in range(len(nodeList)):
				for ii in range(len(nodeList[i][0])):
						nodeList[i][0][ii] -= 1


	#print(nodeList)

	#curMax = 0
	#for i in nodeList:
	#	x = max(i[1])
	#	if x > curMax:
	#		curMax = x

	#makespan += curMax

	#print("Makespan: "+str(float(makespan)/nmbrOfTests))
	#print(str(nodeList[0][1][0]) + '\n')
	#print(str(nodeList[1][1][0]) + '\n')
	#print(str(nodeList[0][1][1]) + '\n')
	#print(str(nodeList[1][1][1]) + '\n')
	#print(len(nodeList[0][1][0]))
	#print(len(nodeList[1][1][0]))

	#print(nodeList)
	#print(len(nodeList))



	# ---- Calculate the makespan, after assignmnet----


	nodeMakespans = [0] * nodes

	slowdowns = [1,1.3,1.5]

	i = 0
	for node in nodeList:
		timeLeft = True

		while timeLeft:
			
			timeLeft = False
			heavyJobs = 0

			for executor in node[1]:
				if executor != []:

					timeLeft = True
					
					#print("exec " + str(executor))

					job = executor[0]

					if job[1]:
						heavyJobs += 1

					time = job[0] - 1
					executor[0] = (time,job[1])

			if timeLeft:
				nodeMakespans[i] += 1*slowdowns[heavyJobs]
			


			#remove all finished jobs

			for executor in node[1]:
				if executor != []:
					jobTime = executor[0][0]
					if jobTime < 1:
						executor.pop(0)
		i += 1
			#if allFree:
			#	break
	makespan += max(nodeMakespans)

print("makespan " + str(float(makespan)/nmbrOfTests))