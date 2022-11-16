import csv
from matplotlib import pyplot as plt

# initate array
discharge = []

#midpoint rule function
#takes an array and a step size h
def midpoint_rule(array, h):
    sum = 0

    for i in range(0,(len(array)-1)):
        #averages each consecutive pairs in array and multiplies by the step size
        avg = (array[i] + array[i+1]) / 2
        sum += avg * h

    return sum

#reads csv file into an array
with open('hooverDailyDischarge.csv', 'r') as csvfile:
    data = csv.reader(csvfile, delimiter='\t')

    for row in data: 
        discharge.append(int(row[1]))
    length = len(discharge)

print("using the midpoint approximation, ", midpoint_rule(discharge,1), " gallons of water flowed through the Hoover damn between 09/13/2020 and 09/13/2021", sep = '')


