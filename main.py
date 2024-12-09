import math
from map import map_nodes





def pathFinder(start, goal, map_nodes):
    visitedNodeList = [[start, None]]
    unvisitedSortedNodesList = [[None, float("inf"), None]] #none->node number, float->cost, none->prev node

    goalCords = map_nodes[goal - 1][1]  
    startCords = map_nodes[start - 1][1] 

    gradient = 0
    intercept = 0

    currentNode = [start]

    foundGoal = [False]

        #find the gradient and the intercept between the line of start node to goal node
    def createStartToGoalLine():
        startX, startY = startCords
        goalX, goalY = goalCords

        gradient = (goalY - startY)/(goalX - startX)

        intercept = startY - (gradient * startX)

    #calculate the cost for a node
    def costOfNode(calNodeNum, goalCords, disToCalNode, gradient, intercept):
        calX, calY = map_nodes[calNodeNum - 1][1]
        goalX, goalY = goalCords
        dSqrd = (gradient * calX - calY + intercept)**2 / (gradient**2 + 1)
        tSqrd = (calX - goalX)**2 + (calY - goalY)**2

        return disToCalNode + dSqrd + tSqrd

    #sort and add the current node's neighbours to the sorted nodes list
    def neighboursCostCal(curNode):
        print("the neghbours that are about to cal belongs to ", curNode)
        curNodeNeighbours =  map_nodes[curNode - 1][2]#looks like [ [neigh number, cost to neigh], [..], ... ] 
        for neighbour in curNodeNeighbours:
            if(neighbour[0] == goal):
                print("found the goal")
                # currentNode[0] = neighbour[0]
                foundGoal[0] = True
                break

            #check if the neighbour has been already calculated and has more than one neighbour
            if(map_nodes[neighbour[0]-1][-1] == False and len(map_nodes[neighbour[0]-1][2]) > 1):
                #has'nt been calculated
                

                print("calculating neighbour ", neighbour)
                #calculate the cost for the current neighbour
                cost = costOfNode(neighbour[0], goalCords, neighbour[1], gradient, intercept)
                map_nodes[neighbour[0]-1][-1] = True
                for index, sortedNode in enumerate(unvisitedSortedNodesList):
                    if(cost <= sortedNode[1]):
                        #put the current neighbour in the sorted nodes list
                        unvisitedSortedNodesList.insert(index, [neighbour[0], cost, currentNode[0]])
                        break
        #all the neighbours of the current node has been put to the sorted nodes list


    #visit next node visit
    def handleNextNodeVisit():
        minNode = unvisitedSortedNodesList[0] #looks like [nodeNum, cost, prevNode]
        print("sorted list: ", unvisitedSortedNodesList)
        print("min node is ", minNode)

        #update visited nodes list
        if(len(visitedNodeList) > minNode[0]):
            visitedNodeList[minNode[0] - 1] = [minNode[0], minNode[2]]
        else:
            while len(visitedNodeList) < minNode[0]-1:
                visitedNodeList.append(None)

            visitedNodeList.append([minNode[0], minNode[2]])

        #set current node to the minimum node of the sorted node list
        currentNode[0] = minNode[0] 

        #remove current node from the sorted node list
        unvisitedSortedNodesList.pop(0)
        

    createStartToGoalLine()

    map_nodes[start-1][-1] = True

    while not foundGoal[0]:
        print("current node in while is ", currentNode[0])
        neighboursCostCal(currentNode[0])  

        print(f"current node is {currentNode[0]} and goal is {goal} before handler")

        # handleNextNodeVisit() if currentNode[0] != goal else None
        # handleNextNodeVisit() if not foundGoal[0] else None
        if not foundGoal[0]:
            handleNextNodeVisit()
        else:
            print(visitedNodeList)
            print("goal minus one is ", goal - 2)

            # visitedNodeList[goal - 2] = [goal, currentNode[0]]

    print(visitedNodeList)
    foundPath = [goal]
    makingPath = True
    nodeInserting = currentNode[0] #at this state nodeInserting = final node before goal 
    #add final node before goal node to the found path list
    foundPath.insert(0, nodeInserting)

    while makingPath:
        if(foundPath[0] != start):
            foundPath.insert(0, visitedNodeList[nodeInserting-1][1])
            nodeInserting = visitedNodeList[nodeInserting-1][1]

        else:
            makingPath = False
        print(foundPath)
        print("inserting node ", nodeInserting)
    
    print(foundPath)
    print("algorithm ended")

pathFinder(19,2, map_nodes)