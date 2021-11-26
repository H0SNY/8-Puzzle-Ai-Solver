from collections import deque
import heapq
import math

initialState = []
goalStates=[
    [0, 1, 2, 3, 4, 5, 6, 7, 8] , 
    [1, 0, 2, 3, 4, 5, 6, 7, 8] , 
    [1, 2, 0, 3, 4, 5, 6, 7, 8] , 
    [1, 2, 3, 0 , 4, 5, 6, 7, 8] , 
    [1, 2, 3, 4 , 0, 5, 6, 7, 8] , 
    [1, 2, 3, 4, 5 , 0, 6, 7, 8] , 
    [1, 2, 3, 4, 5, 6 , 0, 7, 8] , 
    [1, 2, 3, 4, 5, 6, 7 , 0, 8] , 
    [1, 2, 3, 4, 5, 6, 7, 8 , 0] , 
]
moveTrace = []

def puzzleTo2d(state):
    goalState = goalStates[0].copy()
    goalState.pop(0)
    copyState = state.copy()
    index = copyState.index(0)
    copyState.pop(index)
    current = [[]]
    currentGoal = [[]]
    finished = False
    for i in range(3):
        if finished : break
        current.append([])
        currentGoal.append([])
        for j in range(3):
            if i == 2 and j == 2:
                finished = True
                break
            current[i].append(copyState[i * 3 + j])
            currentGoal[i].append(goalState[i * 3 + j])
    currentGoal.pop(len(currentGoal) - 1)
    current.pop(len(current) - 1)
    return [current , currentGoal]

def getManhatten(state):
    [current , currentGoal] = puzzleTo2d(state)
    distance = 0
    for i in range(3):
        for j in range(3):
           if i ==2 and j == 2 : break
           for k in range(3):
               for m in range(3):
                   if k == 2 and m == 2: break
                   if currentGoal[k][m] == current[i][j]:
                       distance = distance + (abs(i - k) + abs(j - m))
    return distance
                   
def getEuclidean(state):
    [current , currentGoal] = puzzleTo2d(state)
    distance = 0
    for i in range(3):
        for j in range(3):
           if i ==2 and j == 2 : break
           for k in range(3):
               for m in range(3):
                   if k == 2 and m == 2: break
                   if currentGoal[k][m] == current[i][j]:
                       distance = distance + (math.sqrt((i - k)**2) + math.sqrt((j - m)**2)  )
    return distance

def checkInversion(state):
    copy = state.copy()
    zero = copy.index(0)
    copy.pop(zero)
    count = 0
    for i in range(7):
        for j in range(i + 1 , 8):
            if copy[j] < copy[i] :
                 count = count + 1
    return count

def switch(list,index1,index2):
    newList=[]
    for i in range(len(list)):
        newList.append(list[i])

    temp=newList[index1]
    newList[index1]=newList[index2]
    newList[index2]=temp
    return newList

def getNextStates(state):
    nextStates=[]
    length=len(state)
    emptyTile=0
    for i in range(length):
        if state[i]==0:
            emptyTile=i
            #    1
            # 0  3
    if emptyTile==0:
        nextStates.append(switch(state,0,1))
        nextStates.append(switch(state, 0, 3))
    elif emptyTile==1:
        nextStates.append(switch(state, 1, 0))
        nextStates.append(switch(state, 1, 4))
        nextStates.append(switch(state, 1, 2))
    elif emptyTile==2:
        nextStates.append(switch(state, 2, 1))
        nextStates.append(switch(state, 2, 5))
    elif emptyTile==3:
        nextStates.append(switch(state, 3, 0))
        nextStates.append(switch(state, 3, 4))
        nextStates.append(switch(state, 3, 6))
    elif emptyTile==4:
        nextStates.append(switch(state, 4, 3))
        nextStates.append(switch(state, 4, 1))
        nextStates.append(switch(state, 4, 5))
        nextStates.append(switch(state, 4, 7))
    elif emptyTile==5:
        nextStates.append(switch(state, 5, 2))
        nextStates.append(switch(state, 5, 4))
        nextStates.append(switch(state, 5, 8))
    elif emptyTile==6:
        nextStates.append(switch(state, 6, 3))
        nextStates.append(switch(state, 6, 7))
    elif emptyTile==7:
        nextStates.append(switch(state, 7, 6))
        nextStates.append(switch(state, 7, 4))
        nextStates.append(switch(state, 7, 8))
    else:
        nextStates.append(switch(state, 8, 7))
        nextStates.append(switch(state, 8, 5))

    return nextStates


def hashState(state):
    hash = ''
    for i in range(len(state)):
        hash = hash + str(state[i])
    return hash
def unHashState(hash):
    state = []
    for i in range(len(hash)):
        state[i] = int(hash[i])
    return state

def breadthFirst(initialState):
    exploredCount = 1
    visitedCount = 0
    frontier = []
    frontier.append(initialState)
    explored=set()
    while len(frontier) > 0:
        state=frontier.pop(0)
        hash = hashState(state)
        explored.add(hash)
        visitedCount += 1
        if state in goalStates:
            return [state , exploredCount , visitedCount]
        nextStates=getNextStates(state)
        for i in range(len(nextStates)):
            nexthash = hashState(nextStates[i])
            if  not nexthash in explored and not nextStates[i] in frontier:
                frontier.append(nextStates[i])
                exploredCount += 1
    print(explored)
    return [initialState , exploredCount , visitedCount , explored]

def depthFirst(initialState):
    exploredCount = 1
    visitedCount = 0
    frontier=[]
    frontier.append(initialState)
    explored=[]
    while len(frontier) > 0:
        state=frontier.pop()
        explored.append(state)
        visitedCount = visitedCount + 1
        if state in goalStates:
            return [state , exploredCount , visitedCount]
        nextStates=getNextStates(state)
        for i in range(len(nextStates)):
            if not nextStates[i] in frontier and not nextStates[i] in explored:
                frontier.append(nextStates[i])
                exploredCount = exploredCount + 1

    return [initialState , exploredCount , visitedCount]    



def a_star(initalState , type):
    exploredCount = 1
    visitedCount = 0
    gloabalHuristicCost = 0
    frontier = []
    heapq.heapify(frontier)
    heapq.heappush(frontier , [ 0 , initalState])
    explored = []
    while len(frontier) > 0:
        print(len(frontier))
        [currCost , state] = heapq.heappop(frontier)
        gloabalHuristicCost = gloabalHuristicCost + currCost
        explored.append(state)
        visitedCount = visitedCount + 1
        if state in goalStates:
            return [state , exploredCount , visitedCount]
        nextStates = getNextStates(state)
        for i in range (len(nextStates)):
            if not nextStates[i] in frontier and not nextStates[i] in explored :
                cost = 0
                if type == 0 : cost = getManhatten(nextStates[i])
                else : cost  = getEuclidean(nextStates[i])
                print("manh : " , getManhatten(nextStates[i]) , "Euc : " , getEuclidean(nextStates[i]))
                heapq.heappush(frontier , [cost , nextStates[i]])
                exploredCount = exploredCount + 1
    
    return [initalState , exploredCount , visitedCount , gloabalHuristicCost]



