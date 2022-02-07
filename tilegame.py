import numpy as np
import random
from itertools import permutations
from copy import deepcopy
import matplotlib.pyplot as plt
from datetime import datetime

keydrop = []

_permutedgrid_dict= {}

#generate board
grid = np.arange(1, 10)
#generate permuations
lst = list(permutations(grid))
lst = [''.join(map(str, g)) for g in lst]
base_permutedgrid_dict = {lst[i]: 0 for i in range(len(lst))}

startingkeys = len(base_permutedgrid_dict)

def calcTargCell(currPosition, currMove):
    cellChange = [1,0]
    if currMove[0] == 'horiz':
        cellChange = [0,1]
    if currMove[1] == 'neg':
        cellChange = [i * -1 for i in cellChange]

    return [x + y for x, y in zip(currPosition, cellChange)]

def isValid(targCell, grid):
    if targCell[0] < 0 or targCell[0] >= grid.shape[0]:
        return False
    if targCell[1] < 0 or targCell[1] >= grid.shape[1]:
        return False
    return True

def remove_curr_board_from_permutations(val, _permutedgrid_dict):
    val = tuple(val.flatten())
    val = ''.join(map(str, val))
    if val in _permutedgrid_dict:
        del _permutedgrid_dict[val]
    return _permutedgrid_dict

def swap(currPosition,prevMove, _permutedgrid_dict, grid):
    looper = True
    while looper:
        currMove = [random.choice(['vert','horiz']), random.choice(['neg', 'pos'])]
        if not (prevMove[0] == currMove[0] and prevMove[1] != currMove[1]):
            targCell = calcTargCell(currPosition, currMove)
            if isValid(targCell, grid):
                looper = False
    
    grid[currPosition[0],currPosition[1]], grid[targCell[0],targCell[1]] \
        = grid[targCell[0],targCell[1]], grid[currPosition[0],currPosition[1]]
    currPosition = targCell
    prevMove = currMove
    
    _permutedgrid_dict = remove_curr_board_from_permutations(grid, _permutedgrid_dict)
    return currPosition, prevMove, _permutedgrid_dict, grid

def playxtimes(x):
    for epoch in range(x):
        epochstarttime = datetime.now()
        grid = np.arange(1, 10)
        grid=grid.reshape(3,3)
        _permutedgrid_dict = deepcopy(base_permutedgrid_dict)

        currPosition = [grid.shape[0]-1,grid.shape[1]-1]    
        prevMove = ['blah','blah']
        _permutedgrid_dict = remove_curr_board_from_permutations(grid, _permutedgrid_dict)
        for i in range(10*startingkeys):
            if i < 0:
                print(i, grid.flatten())
            currPosition,prevMove, _permutedgrid_dict, grid = swap(currPosition,prevMove, _permutedgrid_dict, grid)
            
        endingkeys = len(_permutedgrid_dict)
        changeinkeys = startingkeys - endingkeys
        keydrop.append(changeinkeys)
        print('epoch: ' + str(epoch) + \
            ' delta: ' + str(changeinkeys) + \
            ' runtime: ' + str(datetime.now() - epochstarttime))

x = 1000
print('playtime starts now! \r\n')
playxtimes(x)

plt.plot(keydrop)