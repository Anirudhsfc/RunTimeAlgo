import numpy as np 
import array
import time as t
import matplotlib.pyplot as plt



def GraphOfMyAlgo(Algo,argumentNumber,arrOfRange):
    #To check if the user has entered the range that justifies the number of arguments
    if argumentNumber!=len(arrOfRange)/2:
        print("Please enter the range corresponding to the number of arguments")
        exit()
    k=0
    diffArr=[]
    #To check if there is the same difference between the ranges 
    for i in range(0,argumentNumber):
        diff=arrOfRange[k+1]-arrOfRange[k]
        k=k+2
        diffArr.append(diff) #diffArr stores the value of the range
    element=diffArr[0]

    for i in range(0,len(diffArr)):
        if diffArr[i]!=element:
            print("Please enter the ranges which have the same difference")
            exit()

    
    k=0
    argumentArray=[] #stores the value of the  arguments that need to be passed
    
    for i in range(0,argumentNumber):
        argument_i=np.arange(arrOfRange[k],arrOfRange[k+1],1) #to store the full range of numbers specified for each argument
        k=k+2
        argumentArray.append(argument_i)
    
    timeTaken=[] #to store the time taken by the Algorithm to run
    for i in range(0,(arrOfRange[1]-arrOfRange[0])):
        l=0
        c=0
        unpackThis=[] #We store the vargument values that need to be passed in an array. Example: if there are two arguments and argument1 takes the values a1,a2,a3,...an and the secomnd argument takes the values b1,b2,b3,b4...,bn then the unpackThis stores one of  {a1,b1},{a2,b2},{a3,b3},...{an,bn} in n  iterations
        while c<argumentNumber:
            unpackThis.append(argumentArray[l][i])
            l=1
            c=c+1
        
        start=float(t.time())
        ans=Algo(*unpackThis) #we unpack our set of numbers here using the * operator
        end=float(t.time())
        runTime=float(end-start)
        timeTaken.append(runTime)



    
    
    xAxis=np.arange(arrOfRange[0],arrOfRange[1],1) #We take the x-Axis by default as the range for which the first argument is passed
    #customising graph
    plt.plot(xAxis,timeTaken,label="Your Algorithm")
    plt.xlabel('Values of Input')
    plt.ylabel('Running time')
    plt.ylim(-0.1,3.5)
    plt.xlim(0,arrOfRange[1])
    plt.legend()
    plt.title(' Graph For Running Time of Your Algorithm')
    plt.show()





