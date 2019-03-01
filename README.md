# RunTimeAlgo
This Algorithm is a Python based Algorithm that displays the graph of the running time of the Algorithm that takes any number of Integer type arguments.
All you need to do is run the following lines in your Algorithm.py

from MakeYourOwnGraph import *
#Your_Algorithm_Here
GraphOfMyAlgo(Algorithm_Name(type Function),NumberOfArguments(type int),ArrayOfRangeForTheArguments_Separated_By_Commas)


On running the above commands and running your Algorithm.py you can see the graph generated in Python.

Arguments of the function GraphOfMyAlgo are-

Algorithm_Name- Name of the algorithm fucntion
NumberOfArguments- an Integer value specifying the number of Arguments you have in your Function
ArrayOfRangeForTheArguments_Separated_By_Commas- An array of range for the arguments consisting of beginning and ending of the range. Example: If the number of Arguments are 2 and the range for the first argumet is 1-30 and the second argument is 31-60 then the Array will be [1,30,31,60].

Note: user needs to inpiut the same number of values for the range for all arguments as the function has to run that many times.
Note: The Arguments need to be of int type only

For convenience I have added a UserAlgorithm.py for reference which has an Algorithm for Fibonacci Numbers and displays the graph for the values given.
