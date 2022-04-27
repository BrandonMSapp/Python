"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

This module contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles with a single solution
    where the blank is in the center, e.g.:
        123
        4 5
        678
    When multiple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
"""

import math

class BreadthFirst:
    "BreadthFirst - breadth first search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        # depth, how far the childnode is from initial state
        #Node.expand(parentnode)
        return parentnode.depth + 1
    
    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        # compare searchnode to goal state and find how many tiles are out of place
        # what would h be if we have multiple goal states? Do we import goal state?
        return 0




class DepthFirst:
    "BreadthFirst - breadth first search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        return 0
    
    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        # negative depth
        return -1*(searchnode.depth)



class Manhattan:
    "BreadthFirst - breadth first search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        return parentnode.depth + 1
    
    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        length = 0
        for i in searchnode.state.state_tuple():
            length = length + 1
        # find the row and column lengths using square root of length of entire tuple
        dims = math.sqrt(length)
      
        hcost = 0
        # compute the manhattan distance h(n)
        for s, g in ((searchnode.state.state_tuple().index(i), searchnode.problem.goals[0].index(i)) for i in range(1, length)):
            hcost = hcost + abs(s%dims - g%dims) + abs(s//dims - g//dims)

        return hcost





# To complete:
# Write two more classes, DepthFirst and Manhattan
# that support appropriate g/h with the same signatures for the class functions