BOARD_SIZE = 9

def isPossible(walls, A, B):
    """ Return if a move from A to B is possible 
    A and B are coordinate tuples
    """
    
    # Check if B is a valid space
    if B[0] < 0 or B[0] >= BOARD_SIZE or B[1] < 0 or B[1] >= BOARD_SIZE: return False

    # Check if B is 1 away from A, then check for walls
    if A[0] == B[0]:
        dir = A[1] - B[1]
        if dir == 1: 
            # Down, check for Horizontal walls bottom left and right
            if A[0] != 0 and walls[A[0] - 1, A[1]] == 2: return False
            if A[0] != BOARD_SIZE - 1 and walls[A[0], A[1]] == 2: return False
        elif dir == -1: 
            # Up, check for Horizontal walls top left and right
            if A[0] != 0 and walls[A[0] - 1, A[1] - 1] == 2: return False
            if A[0] != BOARD_SIZE - 1 and walls[A[0], A[1] - 1] == 2: return False
        else: return False

    elif A[1] == B[1]:
        dir = A[0] - B[0]
        if dir == 1: 
            # Right, check for Vertical walls right top and bottom
            if A[1] != 0 and walls[A[0], A[1] - 1] == 1: return False
            if A[1] != BOARD_SIZE - 1 and walls[A[0], A[1]] == 1: return False
        elif dir == -1: 
            # Left, check for Vertical walls left top and bottom
            if A[1] != 0 and walls[A[0] - 1, A[1] - 1] == 1: return False
            if A[1] != BOARD_SIZE - 1 and walls[A[0] - 1, A[1]] == 1: return False
        else: return False
    else:
        return False
    return True