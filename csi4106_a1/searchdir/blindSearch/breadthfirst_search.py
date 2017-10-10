from searchdir.node import *
from searchdir.util import *

## This method must implement Breadth-first search (BFS)
## It must return the solution node and the number of visited nodes
def breadthfirst_search(initialState):
    print('BFS------------------------------')
    '''
    unmark all vertices
    choose some starting vertex x
    mark x
    list L = x
    tree T = x
    while L nonempty
    choose some vertex v from front of list
    visit v
    for each unmarked neighbor w
        mark w
        add it to end of list
        add edge vw to T
    '''
    
    nodesvisited = 0
    
    T = node (initialState)
    
    Q = Queue()
    
    Q.enqueue(T)
    
    while !Q.isEmpty():
        
        v = Q.dequeue()
        
        for w in v.state.possibleActions():
            
            N = node(w,True,v.getcost()+1,v)
            nodesvisited++
            Q.enqueue(N)
            
            if N.state.isgoal():
                return N, nodesvisited
            
    




