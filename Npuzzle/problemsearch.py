'''
problemsearch - Functions for seaarching.
'''

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.timer import Timer
from basicsearch_lib02.searchrep import Problem
from explored import Explored
    
       
def graph_search(problem, verbose=False, debug=False):
      # initialize and start timer
      s = Timer()
      s.__init__()
      # initialize an explored set
      explored = Explored()
      done = False
      # initialize a frontier set as a priority queue
      frontier = PriorityQueue()
      # add initial node to frontier
      node1 = Node(problem, problem.initial)
      frontier.append(node1)

      while (done == False):
            curr = frontier.pop()
            # add node to explored set if it doesn't already exist
            if (explored.exists(curr.state.state_tuple()) == False):
                  explored.add(curr.state.state_tuple())
              
            # check if the current state is a goal state and return solution if it is
            if curr.state.state_tuple() in problem.goals:
                  solution = (len(curr.solution()), len(explored.exploredSet) + frontier.__len__(), s.elapsed_s())
                  done = True
                  return solution
            else:     
                  # when current state is not a goal state, expand its children and check which ones were already explored          
                  children = curr.expand(curr.problem)
                  for i in children:  
                        if explored.exists(i.state.state_tuple()):
                              children.remove(i)
                  # add the children that have not yet been explored to the frontier set     
                  for i in children:
                        frontier.append(i)
                  if frontier.__len__() == 0:
                        done = True
                        return "No Solution"
      
      
"""graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored, elapsed_s) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    elapsed_s is the elapsed wall clock time performing the search
    """
    
          

   
    