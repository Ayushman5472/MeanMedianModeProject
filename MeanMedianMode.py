import csv
from collections import Counter
import statistics

#MEAN
with open('data.csv') as data:
    read = csv.reader(data)
    projectData = list(read)

projectData.pop(0)
weights = []
for i in range(len(projectData)):
    pounds = projectData[i][2]
    weights.append(float(pounds))

length = len(weights)
total = 0
for weight in weights:
    total = total + weight

mean = total/length
print(mean)


#MEDIAN
weights.sort()
if length % 2 == 0:
    Value1 = float(weights[length//2-1])
    Value2 = float(weights[length//2])
    Median = Value1/2 + Value2/2
else:
    Median = weights[(length+1)/2]
print(Median)


#MODE
#I was confused in mode
mode = statistics.mode(projectData)
print(mode)
