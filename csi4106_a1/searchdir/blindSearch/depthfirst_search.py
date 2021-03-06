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
    
    T = Node (initialState)

    if T.state.isGoal():
        return T, nodesvisited
    
    S = Stack()
    
    S.push(T)
    
    while not S.isEmpty():
        
        v = S.pop() 
        
        for w in v.state.possibleActions():
            
            N = Node(v.state.executeAction(w),w,v.getcost()+1,v)

            # if N.g>900:
            #     print ("recursion depth exceeded")
            #     return None, nodesvisited
            try:
                if N.isRepeated():
                    continue
            except RuntimeError:
                print("recursion depth exceeded")
                print("depth of tree: ",N.g)
                return None, nodesvisited
                
            nodesvisited+=1
            S.push(N)
            
            if N.state.isGoal():
                return N, nodesvisited

    print ("solution not found")

    return None, None
    
    
