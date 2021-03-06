
from operator import attrgetter
from searchdir.node import *
from searchdir.util import PriorityQueue

## This method must implement A* search
## It must return the solution node and the number of visited nodes
def astar_search(initialState):
    print('A* ------------------------------------')
    # A* Search Algorithm

    nodesvisited = 0
    
    T = Node (initialState)

    if T.state.isGoal():
        return T, nodesvisited
    
    Q = PriorityQueue()
    
    Q.enqueue(T)
    
    while not Q.isEmpty():
        
        v = Q.dequeue()
        
        for w in v.state.possibleActions():

            N = Node(v.state.executeAction(w), w, v.getcost() + 1, v)

            if N.isRepeated():
                continue

            nodesvisited+=1
            Q.enqueue(N)
            
            if N.state.isGoal():
                return N, nodesvisited

    print ("no solution found")

    return  None, None
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
