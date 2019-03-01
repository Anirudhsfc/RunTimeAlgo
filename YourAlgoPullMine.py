from MakeYourOwnGraph import *





def F1(x,y):
    
    if x<=2:
        return 1
    else:
        return F1(x-1,y)+F1(x-2,y)

GraphOfMyAlgo(F1,2,[1,30,2,31])