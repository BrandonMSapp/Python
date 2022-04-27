# We the undersigned promise that we have in good faith attempted to follow the principles of pair programming. 
# Although we were free to discuss ideas with others, the implementation is our own. 
# We have shared a common workspace (possibly virtually) and taken turns at the keyboard for the majority of the work that we are submitting. 
# Furthermore, any non programming portions of the assignment were done independently. 
# We recognize that should this not be the case, we will be subject to penalties as outlined in the course syllabus. [Brandon Sapp, Isaac Palmer]





from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv, mac
from backtrack import backtracking_search


for puzzle in [easy1, harder1]:
    s = Sudoku(puzzle)     # construct a sudoku problem
    
    # print the initial state and the state after running AC3
    print("Initial state:")
    s.display(s.infer_assignment())
    print('\n')
    AC3(s)
    print("After AC3:")
    s.display(s.infer_assignment())
    print('\n')

    # if not solved after AC3, run backtracking search
    if s.goal_test(s.curr_domains) == False:
        print("Running backtracking search\n")
        solved = backtracking_search(s,select_unassigned_variable=mrv,inference=mac)
        if solved == None:
            print("No Solutions")
        else:
            print("Solution after backtracking search:")
            s.display(s.infer_assignment())
    





    # solve as much as possible by AC3 then backtrack search if needed
    # using MRV and MAC.
    

