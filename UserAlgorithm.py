from MakeYourOwnGraph import * #user needs to import this line


def F1(x,y):
    
    if x<=2:
        return 1
    else:
        return F1(x-1,y)+F1(x-2,y)

GraphOfMyAlgo(F1,2,[1,30,2,31]) #user needs to execute this line in his or her algorithm where the first argument is the name of the Algorithm Function, here F1
                                #the Second argument is the number of arguments that the algorithm of the user inputs
                                #the third argument is an array of ranges, namely beginning value of range, ending value of range_for_first_argument, beginning value of range_for_second_argument, ending value of range_for_second_argument and so on