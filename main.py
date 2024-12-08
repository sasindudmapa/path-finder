import math

from map import map_nodes

visitedNodeList = []
sortedNodesList = []
calculatedNodesList = []
goalCords = [10, 58] #test 
startX, startY = 3, 23 #test
gradient = 5
intercept = 8

#node structure = [
#                   nodeNum, 
#                   (node cords x, y), 
#                   [[neighbourNum, distance to neighbour], [..] ,... ], 
#                   calculated or not 
#                  ]


#calculate the cost for a node
def costOfNode(calNodeNum, goalCords, disToCalNode, gradient, intercept):
    calX, calY = map_nodes[calNodeNum - 1][1]
    goalX, goalY = goalCords
    dSqrd = (gradient * calX - calY + intercept)**2 / (gradient**2 + 1)
    tSqrd = (calX - goalX)**2 + (calY - goalY)**2

    return disToCalNode + dSqrd + tSqrd


# print(costOfNode(1, [10, 58], 8, 5, 8))


#sort and add the current node's neighbours to the sorted nodes list
def neighboursCostCal(curNode):
    curNodeNeighbours = curNode[2] #looks like [ [neigh number, cost to neigh], [..], ... ] 
    for neighbour in curNodeNeighbours:
        #checking if the neighbour has been already calculated
        if(map_nodes[neighbour[0]-1][-1] == False):
            #has'nt been calculated
            
            #calculate the cost for the current neighbour
            cost = costOfNode(neighbour[0], goalCords, neighbour[1], gradient, intercept)
            for sortedNode in sortedNodesList:
                print()