import numpy as np 
import array
import time as t
import matplotlib.pyplot as plt



def GraphOfMyAlgo(Algo,argumentNumber,arrOfRange):
    
    k=0
    argumentArray=[]
    # print(argumentNumber)
    # print(len(arrOfRange))
    for i in range(0,argumentNumber):
        argument_i=np.arange(arrOfRange[k],arrOfRange[k+1],1)
        k=k+2
        argumentArray.append(argument_i)
    # print(argumentArray)
    timeTaken=[]
    for i in range(0,(arrOfRange[1]-arrOfRange[0])):
        l=0
        c=0
        unpackThis=[]
        while c<argumentNumber:
            unpackThis.append(argumentArray[l][i])
            l=1
            c=c+1
        #print(unpackThis)
        start=float(t.time())
        ans=Algo(*unpackThis)
        end=float(t.time())
        runTime=float(end-start)
        timeTaken.append(runTime)



    
    
    xAxis=np.arange(arrOfRange[0],arrOfRange[1],1)
    # print(xAxis)
    # print(timeTaken)
    # print(len(timeTaken))
    plt.plot(xAxis,timeTaken,label="Your Algorithm")
    plt.xlabel('Values of Input')
    plt.ylabel('Running time')
    plt.ylim(-0.1,3.5)
    plt.xlim(0,arrOfRange[1])
    plt.legend()
    plt.title(' Graph For Running Time of Your Algorithm')
    plt.show()

    # print(argumentArray[0])
    # print(argumentArray[1])
    # print(argumentArray[0][0])
    # print(argumentArray[1][0])



