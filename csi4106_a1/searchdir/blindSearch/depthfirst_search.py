from searchdir.node import *
from searchdir.util import *

## This method must implement depdth-first search (DFS)
## It must return the solution node and the number of visited nodes
def depthfirst_search(initialState):
    print('DFS ----------------------------------')
    '''
    DFS(G,v)   ( v is the vertex where the search starts )
         Stack S := {};   ( start with an empty stack )
         for each vertex u, set visited[u] := false;
         push S, v;
         while (S is not empty) do
            u := pop S;
            if (not visited[u]) then
               visited[u] := true;
               for each unvisited neighbour w of u
                  push S, w;
            end if
         end while
      END DFS()
    '''
    nodesvisited = 0
    
    T = node (initialState)
    
    S = Stack()
    
    S.push(T)
    
    while !S.isEmpty():
        
        v = S.pop() 
        
        for w in v.state.possibleActions():
            
            N = node(v.executeAction(w),w,v.getcost()+1,v)
            
            if N.isRepeated():
                continue 
                
            nodesvisited++
            S.push(N)
            
            if N.state.isgoal():
                return N, nodesvisited
    
    
