import csv
import random
import math
import operator

#calculates euclidian distance
def euclidianDistance(first, second, length):
    distance = 0
    for i in range(1,length):
        distance += pow((first[i] - second[i]), 2)
    return math.sqrt(distance)

def accuracy(testCases, predictions):
    correctAnswers = 0;
    for i in range(len(testCases)):
        if testCases[i][-1] is predictions[i]:
            correctAnswers += 1
    return (correctAnswers/float(len(testCases)))*100.0

# returns K amount of most similar neighbours from training set

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for i in range(len(trainingSet)):
        dist = euclidianDistance(testInstance,trainingSet[i], length)
        distances.append((trainingSet[i], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors

def changetoint(dataset):
        for item in dataset:
            for i in range(1, (len(item))):
                if item[i] == "?":
                    item[i] = int("0")
                else:
                    item[i] = int(item[i])
        return dataset

def giveResponse(neighbours):
    classVotes = {}
    for i in range(len(neighbours)):
        response = neighbours[i][-1]
        if response in classVotes:
            classVotes[response] +=1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

# bringing the data to Python environment
# brings data in as csv and appends

def addData(file, suhde, trainingSet=[] , testSet=[]):
    with open(file, 'rb') as csvfile:
        rivit = csv.reader(csvfile)
        dataset = changetoint(list(rivit))
        for i in range(len(dataset)-1):
            if random.random() < suhde:
                trainingSet.append(dataset[i])
            else:
                testSet.append(dataset[i])

def main():
    trainingSet=[]
    testSet=[]
    split=0.67
    addData('rintasyopa.data', split, trainingSet, testSet)
    print 'training setti ' + repr(len(trainingSet))
    print 'Testing setti ' + repr(len(testSet))
    predictions=[]
    k = 2
    for i in range(len(testSet)):
        neighbours = getNeighbors(trainingSet,testSet[i], k)
        result = giveResponse(neighbours)
        predictions.append(result)
        print('ennustettu: ' + repr(result) + ', toteutunut' + repr(testSet[i][-1]))
    prosentti = accuracy(testSet, predictions)
    print('ennustamisprosentti ' + repr(prosentti) + '%')

main()