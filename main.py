import numpy as np

""" Walls are denoted by their center point. 
1 = vertical wall, 2 = horizontal.
"""
walls = np.zeros((8,8))
pieces = [(0, 4), (8, 4)] # Starting Positions
wallCount = [10, 10]
