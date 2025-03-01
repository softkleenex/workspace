'''
All the cool kids in town want to become a member of the Bots and Androids Programmer Club (BAPC). To become a member of the club, applicants must show a feat of their skills with a home-made robot that is programmed to perform some tricks. Just like your older brother, you want to become a member of the BAPC, so it's time to lock yourself in the hobby basement and start building some robots!

Since your older brother has used up almost all of the parts for his own projects at the BAPC, you will have to get creative with whatever is still left. You find a robotic arm that has only a single purpose: fitting circle-shaped objects into square-shaped holes. Not exactly what you had in mind, but it will have to do. After all, you only have five hours left to apply for your BAPC membership.

The memory chip of the robotic arm seems to be wiped, but luckily you do know the programming interface of its ARM processor. Firstly, the robotic arm only supports integer coordinates. Secondly, when the arm picks up a circle-shaped object, you need to calculate the smallest possible square that it could fit the object in, after which it will autonomically find a suitable square-shaped hole.

Given the location of a circle-shaped object, calculate the smallest possible square which encloses the object.

입력
The input consists of:

One line containing two integers 
$x$ and 
$y$ (
$-10^9leq x,yleq 10^9$), the coordinates of the center of the circle.
One line containing one integer 
$r$ (
$1leq rleq 10^9$), the radius of the circle.
출력
Output four lines, each line containing two integers, representing the 
$x$- and 
$y$-coordinates of one of the corners of the square. The coordinates should be printed in either clockwise or counter-clockwise order.

If there are multiple valid solutions, you may output any one of them.

예제 입력 1 
-3 6
5
예제 출력 1 
-10 7
-2 13
4 5
-4 -1
예제 입력 2 
0 0
10
예제 출력 2 
-14 -2
-2 14
14 2
2 -14
'''

x, y = map(int, input().split())
r = int(input())
print(x + r, y + r)
print(x +r, y - r)
print(x -r, y - r)
print(x -r, y + r, end = '')