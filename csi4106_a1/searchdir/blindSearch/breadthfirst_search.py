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
    
    T = Node (initialState)
    
    Q = Queue()
    
    Q.enqueue(T)
    
    while not Q.isEmpty():
        
        v = Q.dequeue()
        
        for w in v.state.possibleActions():
            
            N = Node(v.executeAction(w),w,v.getcost()+1,v)
            
            if N.isRepeated():
                continue 
                
            nodesvisited+=1
            Q.enqueue(N)
            
            if N.state.isgoal():
                return N, nodesvisited
            
    




