### Author: Amal Zouaq
### azouaq@uottawa.ca
## Author: Hadi Abdi Ghavidel
## habdi.cnlp@gmail.com

import timeit

import numpy as np
import random
from searchdir.blindSearch.breadthfirst_search import *
from searchdir.blindSearch.depthfirst_search import *
from searchdir.heuristicSearch.astar_search import *
from searchdir.state import *


class EightPuzzleState(State):

    #initializes the eight puzzle with the configuration passed in parameter (numbers)
    def __init__(self, numbers):
        self.numbers = numbers



    #returns a boolean value that indicates if the current configuration is the same as the goal configuration
    def isGoal(self):
        if self.numbers == [0,1,2,3,4,5,6,7,8]:
            return True
        else:
            return False


    # returns the set of legal actions in the current state
    def possibleActions(self):
        possible = []
        
        #find position of 0 in numbers
        num = self.numbers.index(0)
        
        #left
        if num % 3 != 0:
            possible.append('left')
        
        #right
        if num % 3 != 2:
            possible.append('right')
            
        #up
        if num > 2:
            possible.append('up')
        
        #down
        if num < 5:
            possible.append('down')

        return possible


    # applies the result of the move on the current state
    def executeAction(self, move):
        
        newState = EightPuzzleState(self.numbers[:])
        
        if move == 'left':
            tempindex = self.numbers.index(0)
            newState.numbers[tempindex]=self.numbers[tempindex - 1]
            newState.numbers[tempindex - 1]=0
        
        elif move == 'right':
            tempindex = self.numbers.index(0)
            newState.numbers[tempindex]=self.numbers[tempindex + 1]
            newState.numbers[tempindex + 1]=0
        
        elif move == 'up':
            tempindex = self.numbers.index(0)
            newState.numbers[tempindex]=self.numbers[tempindex - 3]
            newState.numbers[tempindex - 3]=0
        
        elif move == 'down':
            tempindex = self.numbers.index(0)
            newState.numbers[tempindex]=self.numbers[tempindex + 3]
            newState.numbers[tempindex + 3]=0
        
        else:
            raise "illegal move"
            
        return newState


    # returns true if the current state is the same as other, false otherwise
    def equals(self, other):
        if self.numbers == other.numbers:
            return True
        else:
            return False


    # prints the grid representing the current state
    # e.g. -----------
        # |   | 1 | 2 |
        # -----------
        # | 3 | 4 | 5 |
        # -----------
        # | 6 | 7 | 8 |
        # -----------
    def show(self):
    # TO COMPLETE
        print("-----------") 
        for i in range (3):
            print("|"+str(self.numbers[i*3+0])+"|"+str(self.numbers[i*3+1])+"|"+str(self.numbers[i*3+2])+"|")
        print("-----------")

    # returns the cost of the action in parameter
    def cost(self, action):
    # TO COMPLETE
        return 1

    # returns the value of the heuristic for the current state
    # note that you can alternatively call heuristic1() and heuristic2() to test both heuristics with A*
    def heuristic(self):
        #return self.heuristic1()
        return self.heuristic2()


    ## returns the value of your first heuristic for the current state
    # make sure to explain it clearly in your comment
    def heuristic1(self):
        #this is the manhattan distance
        dist = 0

        for i in range(len(self.numbers)):
            dist += abs((i%3) - (self.numbers.index(i)%3))
            
            dist += abs(int(i/3) - int(self.numbers.index(i)/3))

        return dist

    # returns the value of your first heuristic for the current state
    # make sure to explain it clearly in your comment
    def heuristic2(self):
        count = 0
        for i in range (9):
            if self.numbers[i]!=i:
                count +=1

        return count


####################### SOLVABILITY ###########################

def issolvable(puzzle):
    puzzle_str = np.array(list(map(int, puzzle)))
    print("Puzzle string: ", puzzle_str)
    if inversions(puzzle_str) % 2:
        return False
    else : return True

def inversions(s):
    k = s[s != 0]
    return sum(
        len(np.array(np.where(k[i + 1:] < k[i])).reshape(-1))
        for i in range(len(k) - 1)
    )

def randomize(puzzle):
    puzzle = puzzle.shuffle_ran(puzzle, 1)
    puzzle_choice = []
    for sublist in puzzle.cells:
        for item in sublist:
            puzzle_choice.append(item)
    return puzzle, puzzle_choice

    def shuffle_ran(self,board, moves):
        newState = board
        if moves==100:
            return newState
        else:
            newState.executeAction(random.choice(list(board.possibleActions())))
            moves= moves+1
            return self.shuffle_ran(newState, moves)

#######  SEARCH ###########################
EIGHT_PUZZLE_DATA = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
                     [1, 0, 2, 3, 4, 5, 6, 7, 8],
                     [1, 0, 2, 3, 4, 5, 8, 7, 6],
                     [4, 0, 6, 1, 2, 8, 7, 3, 5],
                     [1, 2, 8, 7, 3, 4, 5, 6, 0],
                     [5, 1, 3, 4, 0, 2, 7, 6, 8],
                     [1, 2, 5, 7, 6, 8, 0, 4, 3],
                     [4, 6, 0, 7, 2, 8, 3, 1, 5]]

puzzle_choice = EIGHT_PUZZLE_DATA[3]
puzzle = EightPuzzleState(puzzle_choice)
#puzzle, puzzle_choice = randomize(puzzle)
print('Initial Config')
puzzle.show()
if not issolvable(puzzle_choice):
    print("NOT SOLVABLE")
else:
    start = timeit.default_timer()
    solution, nbvisited = breadthfirst_search(puzzle)
    stop = timeit.default_timer()
    printResults('BFS', solution, start, stop, nbvisited)


    start = timeit.default_timer()
    solution, nbvisited = depthfirst_search(puzzle)
    stop = timeit.default_timer()
    printResults('DFS', solution, start, stop, nbvisited)

    start = timeit.default_timer()
    solution, nbvisited = astar_search(puzzle)
    stop = timeit.default_timer()
    printResults('A*', solution, start, stop, nbvisited)


