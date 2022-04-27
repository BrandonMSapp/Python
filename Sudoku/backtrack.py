

from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)


def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
   assignment = csp.infer_assignment()    # initialize assignment list
   if len(assignment) == 81:     # return assignment list if all variables have been assigned
      return (assignment,csp.nassigns)
   var = select_unassigned_variable(assignment,csp)     # choose variable using mrv heuristic
   for x in order_domain_values(var,assignment,csp):    # iterate through the variables domain
      if csp.nconflicts(var,x,assignment) == 0:    # check if domain value is consistent and assign to variable if so
         csp.assign(var,x,assignment)
         remove = csp.suppose(var,x)    # get list of removed values using suppose method
         inferences = inference(csp,var,x,assignment,remove)    # use mac to propagate constraints
         if inferences != False:    # if AC3 does not return false, recursively call backtrack
            result = backtracking_search(csp,select_unassigned_variable,unordered_domain_values,inference)
            if result != None:     # if backtracking search does not fail, return the result of the search   
               return result
         csp.restore(remove)    # if inferences is false, restore removed values
         assignment.pop(var)    # remove prior assignment from assignment list
   return None


    
   # """backtracking_search
   # Given a constraint satisfaction problem (CSP),
   # a function handle for selecting variables, 
   # a function handle for selecting elements of a domain,
   # and a function handle for making inferences after assignment,
   # solve the CSP using backtrack search

   # Returns two outputs:
   #    dictionary of assignments or None if there is no solution
   #    Number of variable assignments made in backtrack search (not counting
   #    assignments made by inference)
   # """
    
    # See Figure 6.5 of your book for details
