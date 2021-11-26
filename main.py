from collections import deque

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


def breadthFirst(initialState):
    exploredCount = 1
    visitedCount = 0
    frontier = []
    frontier.append(initialState)
    explored=[]
    print("Staring Dequing....")
    while len(frontier) > 0:
        print(len(frontier))
        state=frontier.pop(0)
        print("dequed : " , state)
        explored.append(state)
        print("appended in explored and visitedCount incremented")
        visitedCount += 1
        if state in goalStates:
            print("State Is Accomplished")
            return [state , exploredCount , visitedCount]
        nextStates=getNextStates(state)
        print("possible Next States : " , nextStates)
        for i in range(len(nextStates)):
            print('Checking Child in explored  : ' , nextStates[i] in explored)
            print('checking Child in visited : ' ,nextStates[i] in frontier )
            if  not nextStates[i] in explored:
                if not nextStates[i] in frontier:
                    print("not in visited or explored , enqueue")
                    frontier.append(nextStates[i])
                    exploredCount += 1
 
    return [initialState , exploredCount , visitedCount]

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







