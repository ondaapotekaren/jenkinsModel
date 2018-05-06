import sys
import numpy


it = int(sys.argv[1])

for exe in range(1,11):
	acc = 0
	for jj in range(0,it):
		s =  (numpy.random.pareto(2,100) + 1)

		q = []

		for i in s:
			q.append(int(i*100))
		
		if sys.argv[2] == "SJF":
			q = sorted(q)
		if sys.argv[2] == "LJF":
			q = sorted(q)
			q.reverse()

		curList = [0] * exe 
		accList =[0] * exe

		while len(q) > 0:
			for i in range(len(curList)):
				if curList[i] == 0:
					if len(q) > 0: 
						temp = int(q.pop(0))
						curList[i] = temp
						accList[i] = accList[i] + temp
				curList[i] = curList[i] - 1

		acc += max(accList)
	f = open("stat"+sys.argv[2],'a')
	f.write(str(exe) + " " +str(float(acc)/it) + '\n')
	f.close()
