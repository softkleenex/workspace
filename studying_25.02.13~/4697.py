# 문제
# A contractor is planning to bid on interior painting for an apartment. These apartments are for student housing, so they are to be single-room efficiencies and have basic drywall walls and ceilings, with no particular architectural features like crown molding. He would like to find a quicker way to estimate how much paint it will take to paint the walls and ceilings for each job. The plan for these buildings is to paint the four walls and the ceiling. Of course, no paint is needed for window and door openings. All rooms, windows and doors are rectangular. All rooms will be painted the same color.

# The contractor will provide you with information about the dimensions of the rooms, the windows and doors for each floor plan, and the number of apartments. Your team is to write a program that will tell him how many cans of paint he should include in his bid.

# 입력
# There will be several test cases in the input. Each test case begins with a line with 6 integers:

# n width length height area m

# where n (1 ≤ n ≤ 100) is the number of apartments, width (8 ≤ width ≤ 100) is the width of each room, length (8 ≤ length ≤ 100) is the length of each room, height (8 ≤ height ≤ 30) is the height of each room, area (100 ≤ area ≤ 1, 000) is the area in square feet that can be covered by each can of paint, and m (0 ≤ m ≤ 10) is the number of windows and doors.

# On each of the next m lines will be two positive integers, width and height, describing a door or window. No window or door will be larger than the largest wall. All linear measures will be expressed in feet. The input will end with a line with six 0’s.

# 출력
# For each test case, output a single integer on its own line, indicating the number of cans of paint needed to paint all of the walls and ceilings of all of the apartments.
import math


while 1:
    a, b, c, d, e, f = list(map(int, input().split()))


    if ([a, b, c, d, e, f] == [0] * 6):
        quit()
  
    x = 0
    x = (b * c + c * d * 2 + d * b * 2)

    for i in range(0 , f):
        temp1, temp2 = list(map(int, input().split()))
        x -= temp1 * temp2


    #print(a, x, f)
    x = math.ceil((a * x ) / e)

    print(x)