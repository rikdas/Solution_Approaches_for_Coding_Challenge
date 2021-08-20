import random
import numpy
import math
import time
import matplotlib.pyplot as plt

def printCommonSyntax():
    print("Algorithm(ObjFunction, LB, UB, Dimension, Population, Iteration)")

def TunePopulation(x):
    y = []
    for i in x:
        y.append(round(i,3))
        #y.append(int(i))
    return y

class solution:
    def __init__(self):
        self.best = 0
        self.leader_solution = []
        self.convergence = []
        self.conv_gen = 0
        self.optimizer = ""
        self.objfname = ""
        self.startTime = 0
        self.endTime = 0
        self.executionTime = 0
        self.lb = 0
        self.ub = 0
        self.dim = 0
        self.popnum = 0
        self.maxiers = 0
        
def printResult(SOLUTION):
    print('Best Fitness :', round(SOLUTION.best,4))
    print('Best Label   :', TunePopulation(SOLUTION.leader_solution))
    print('Exec. Time   :', round(SOLUTION.executionTime,2))
    print('Conv. Time   :', round(SOLUTION.executionTime*SOLUTION.conv_gen/SOLUTION.maxiers, 4))
    
def printConvergence(SOLUTION):
    print('\nConvergence  :\n[', end='')
    for i in SOLUTION.convergence:
        print(round(i,3),', ', sep='', end='')
    print('\b\b]\n')
    
def plotResult(SOLUTION):
    plt.plot(range(1, len(SOLUTION.convergence)+1), SOLUTION.convergence)
    
def appendResult(f, s):
    s.sort(key=(lambda x : round(x.best,4)))
    file = open(f, 'a')
    file.write('\nMethod       : '+str(s[0].optimizer))
    file.write('\nBest Fitness : '+str(round(s[0].best,4)))
    file.write('\nBest Label   : '+str(TunePopulation(s[0].leader_solution)))
    file.write('\nConv. Time   : '+str(round(s[0].executionTime*s[0].conv_gen/s[0].maxiers, 4)))
    file.write('\nConv. Gen    : '+str(round(s[0].conv_gen)))
    
    res1, res2, res3 = [], [], []
    for i in s:
        res1.append(i.best), res2.append(i.executionTime), res3.append(i.executionTime*i.conv_gen/i.maxiers)
    file.write('\nAvg. Fitness : '+str(round(sum(res1)/len(res1), 2)))
    file.write('\nAvg. Conv    : '+str(round(sum(res3)/len(res3), 2)))
    file.write('\nAvg. Exec    : '+str(round(s[0].executionTime, 2)))
    
    file.write('\nThe Curve    : [')
    for i in s[0].convergence:
        file.write(str(i)+', ')
    file.write(']\n')
    
    file.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    