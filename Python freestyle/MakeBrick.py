"""
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops. 

EXAMPLES:
make_bricks(3, 1, 8) True
make_bricks(3, 1, 9) False
make_bricks(3, 2, 10) True

TEST CASES:
make_bricks(3, 1, 8)	True
make_bricks(3, 1, 9)	False
make_bricks(3, 2, 10)	True
make_bricks(3, 2, 8)	True
make_bricks(3, 2, 9)	False
make_bricks(6, 1, 11)	True
make_bricks(6, 0, 11)	False
make_bricks(1, 4, 11)	True
make_bricks(0, 3, 10)	True
make_bricks(1, 4, 12)	False
make_bricks(3, 1, 7)	True
make_bricks(1, 1, 7)	False
make_bricks(2, 1, 7)	True
make_bricks(7, 1, 11)	True
make_bricks(7, 1, 8)	True
make_bricks(7, 1, 13)	False
make_bricks(43, 1, 46)	True
make_bricks(40, 1, 46)	False
make_bricks(40, 2, 47)	True
make_bricks(40, 2, 50)	True
make_bricks(40, 2, 52)	False
make_bricks(22, 2, 33)	False
make_bricks(0, 2, 10)	True
make_bricks(1000000, 1000, 1000100)	True
make_bricks(2, 1000000, 100003)	False
make_bricks(20, 0, 19)	True
make_bricks(20, 0, 21)	False
make_bricks(20, 4, 51)	False
make_bricks(20, 4, 39)	True
"""

def make_bricks(small, big, goal):
    
  """This below commented code passes all the above cases 
  but failed in hidden cases which are unknown"""
  
  # if 5*big > goal:
  #   if goal%5 == small:
  #     return True
  # elif 5*big == goal:
  #   return True
  # else:
  #   if (5*big + small)>=goal:
  #     return True
  # return False
  
  # if (5*big + small)<goal:
  #   return False
  # if goal%5 > small:
  #   return False
  # return True

  if (5*big + small)>=goal and goal%5 <= small:
    return True
  return False

print("make_bricks(%2d,%2d,%2d)"%(6,0,11)+" --> "+str(make_bricks(6,0,11)))