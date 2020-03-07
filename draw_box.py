from box_constants import *

def draw_box(w, h):
    """ 
    Draws a box of size (w, h) 
    
    For a given width and height, this function validates input (width and height must be 
    ints no less than 2). 

    Parameters: 
    w (int): Width of box to be drawn
    h (int): Height of box to be drawn

    Returns: 
    None: draws box directly to stdout
    """

    if not isinstance(w, int) or not isinstance(h, int):
        raise TypeError("Width and height must be integers")

    if w < 2 or h < 2: 
        raise ValueError("Minimum box size is 2x2")

    for h_coord in range(h):
        for w_coord in range(w):
            char_code = get_code(h_coord, w_coord, h, w)
            character = chr(char_code)

            print(character, end="")
            
            if w_coord == w - 1: 
                print("\n", end="")

def get_code(h_coord, w_coord, h, w): 
    """ 
    Return unicode constant for a given (h,w) coordinate 

    For a given height and width coordinate (we construct the box row by row so height and
    width are reversed for simplicity), return the unicode constant for the box component 
    that belongs at that coordinate. Assumed to be called post input validation so makes no 
    additional checks. 

    Parameters: 
    h_coord (int): current height coordinate 
    w_coord (int): current width coordinate 
    h: height of box to be drawn
    w: width of box to be drawn 

    Returns: 
    int: Unicode value from box_constants.py 
    """

    if (h_coord, w_coord) == (0, 0):
        return TOP_LEFT
    elif (h_coord, w_coord) == (0, w-1): 
        return TOP_RIGHT
    elif (h_coord, w_coord) == (h-1, 0): 
        return BOTTOM_LEFT
    elif (h_coord, w_coord) == (h-1, w-1): 
        return BOTTOM_RIGHT
    elif h_coord == 0 or h_coord == h-1:
        return H_EDGE
    elif w_coord == 0 or w_coord == w-1:
        return V_EDGE
    else: 
        return SPACE

if __name__ == "__main__":
    draw_box(3,5)