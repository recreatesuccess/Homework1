## Author: Amal Zouaq
### azouaq@uottawa.ca
### Author: Hadi Abdi Ghavidel
###habdi.cnlp@gmail.com

from operator import attrgetter

#Queue - Implementation of the data structure Queue
class Queue:
    # initializes the current data structure
    def __init__(self):
        self.items = []


    # returns the elements of the current data structure
    def show(self):
        return self.list

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return self.items == []

    # add the element item to the current data structure
    def enqueue(self, item):
        self.items.insert(0,item)


    # removes an element from the current data structure
    def dequeue(self):
        return self.items.pop()

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.items)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        return item in self.list


#Priority Queue Implementation of the data structure PriorityQueue
class PriorityQueue:
    # initializes the data structure
    def __init__(self, fct):
        self.items = []

    # returns the elements of the current data structure
    def show(self):
        return self.list

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return self.list == []

    # add the element item to the current data structure
    def enqueue(self, item):
        self.items.append(item)

    # removes an element from the current data structure
    def dequeue(self):
        min = 0
        for i in range(1, len(self.list)):
            if self.list[i].f < self.list[min].f:
                min = i
        item = self.list.pop(min)
        return item

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.list)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        return item in self.list

#Stack - Implementation of the data structure Stack
class Stack:
    # initializes the data structure
    def __init__(self):
        self.items = []

    # returns the elements of the current data structure
    def show(self):
        return self.list

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return self.items == []

    # add the element item to the current data structure
    def push(self, item):
        self.items.append(item)

    # removes an element from the current data structure
    def pop(self):
        return self.items.pop()

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.items)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        return item in self.list


#Prints results for search alorithms
def printResults(alg, solution, start, stop, nbvisited):
    try:
        result, depth = solution.extractSolutionAndDepth()
        if result != []:
            print("The Solution is  ", (result))
            print("The Solution is at depth ", depth)
            print("The path cost is ", solution.getcost())
            print('Number of visited nodes:', nbvisited)
            time = stop - start
            print("The execution time is ", time, "seconds.")
            print("Done!")
    except AttributeError:
        print("No solution")
    except MemoryError:
        print("Memory Error!")
