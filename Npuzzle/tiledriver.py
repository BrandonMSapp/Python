'''
driver for graph search problem

'''
# Isaac Palmer 822598342 and Brandon Sapp 822246796
# Affidavit: This code was written completely by Isaac and Brandon
from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.timer import Timer
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections



def driver() :
    # Variables to store the sums in order to compute averages
    planLenBreadth, planLenDepth, planLenMan = [], [], []
    numNodesBreadth, numNodesDepth, numNodesMan = [], [], []
    elapsedBreadth, elapsedDepth, elapsedMan = [], [], []
    
    # Iterate 31 times creating 31 different problem states and calling each search strategy 31 times
    for i in range(5):
        print("Running iteration: " + str(i))
        puzzle = NPuzzle(8)
        # breadth_s = NPuzzle(8, force_state=puzzle.initial, g=BreadthFirst.g, h=BreadthFirst.h)
        # depth_s = NPuzzle(8, force_state=puzzle.initial, g=DepthFirst.g, h=DepthFirst.h)
        manhat_s = NPuzzle(8, force_state=puzzle.initial, g=Manhattan.g, h=Manhattan.h)
        # b = graph_search(breadth_s)
        # d = graph_search(depth_s)
        m = graph_search(manhat_s)
        # planLenBreadth.append(b[0])
        # planLenDepth = planLenDepth + d[0]
        planLenMan.append(m[0])
        # numNodesBreadth = numNodesBreadth + b[1]
        # numNodesDepth = numNodesDepth + d[1]
        numNodesMan.append(m[1])
        # elapsedBreadth = elapsedBreadth + b[2]
        # elapsedDepth = elapsedDepth + d[2]
        elapsedMan.append(m[2])
    # Compute and print averages of each search
    print("--Breadth search-- ")
    print("Plan length: " + str(mean(planLenBreadth)) + " +/- " + str(stdev(planLenMan)))
    print("# of nodes: " + str(mean(numNodesBreadth)) + " +/- " + str(stdev(planLenMan)))
    print("Elapsed time: " + str(mean(elapsedBreadth)) + " +/- " + str(stdev(planLenMan)))
    print("--Depth search-- ")
    print("Plan length: " + str(mean(planLenDepth)) + " +/- " + str(stdev(planLenMan)))
    print("# of nodes: " + str(mean(numNodesDepth)) + " +/- " + str(stdev(planLenMan)))
    print("Elapsed time: " + str(mean(elapsedDepth)) + " +/- " + str(stdev(planLenMan)))
    print("--Manhattan search-- ")
    print("Plan length: " + str(mean(planLenMan)) + " +/- " + str(stdev(planLenMan)))
    print("# of nodes: " + str(mean(numNodesMan)) + " +/- " + str(stdev(numNodesMan)))
    print("Elapsed time: " + str(mean(elapsedMan)) + " +/- " + str(stdev(elapsedMan)))




        


# To do:  Run driver() if this is the entry module

driver()