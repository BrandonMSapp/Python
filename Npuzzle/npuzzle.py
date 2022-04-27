# -*- coding: utf-8 -*-

from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.searchrep import Problem

class NPuzzle(Problem):
    """
    NPuzzle - Problem representation for an N-tile puzzle
    Provides implementations for Problem actions specific to N tile puzzles.
    """
    def __init__(self, n, force_state =None, **kwargs):
        """"__init__(n, force_state, **kwargs)
        
        NPuzzle constructor.  Creates an initial TileBoard of size n.
        If force_state is not None, the puzzle is initialized to the
        specified state instead of being generated randomly.
        
        The parent's class constructor is then called with the TileBoard
        instance and any remaining arguments captured in **kwargs.        
        
        """
        
        self.n = n
       # create new tileboard of size n for initial
        new_board = TileBoard(self.n)
        
        # pass the new board to the parent class, kwargs holds the g and h values
        super().__init__(new_board, new_board.goals, **kwargs)
       
      

        # Note on **kwargs:
        # **kwargs is Python construct that captures any remaining arguments 
        # into a dictionary.  The dictionary can be accessed like any other 
        # dictionary, e.g. kwargs[“keyname”], or passed to another function 
        # as if each entry was a keyword argument:
        #    e.g. foobar(arg1, arg2, …, argn, **kwargs).

        
        
    def actions(self, state):
        "actions(state) - find a set of actions applicable to specified state"
        
        return super().actions(state)
        
        
    
    def result(self, state, action):
        "result(state, action)- apply action to state and return new state"
        
        return super().result(state, action)
      
    
    def goal_test(self, state):
        "goal_test(state) - Is state a goal?"

        return super().goal_test(state)

    
        



