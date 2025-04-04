# Figure skating is a very popular sport at the Winter Olympics. It has been on the programme the longest of all winter sports, having even been included in the Summer Olympics before the split in 1924. Just like in gymnastics, each contestant executes a routine consisting of elements, which are individually scored by a jury. This subjective aspect to judging skill always leaves room for heated discussion, but a huge scandal in the 2002 Winter Olympics, with allegations that the game had been fixed, caused a transition to the new scoring system IJS. Points awarded to each element of the routine are known beforehand: A Lutz scores 0.60 points (but 2.10 for a double and 5.90 for a triple), a Salchow scores 0.40 (1.30 for double, 4.30 for triple), an Euler scores 0.50, et cetera. Then, points are added or subtracted by the jury based on execution. Consequently, a figure skater is able to estimate his or her score assuming average performance.

# Olympics observers from the Bookmakers' Association for the Prevention of Cheating are tasked with assessing the objectivity of the jury. They will compare the predicted ranking of the contestants with the final outcome to determine who is the jury's favourite. The favourite is the contestant who rose the most places between the predicted and final scoreboard. Ties are broken by whoever ends up higher on the final scoreboard. However, if no one did better than predicted, this raises some red flags with the observers, which is declared "suspicious".

# 입력
# The input consists of:

# A line containing a single integer $n$ ($1 \leq n \leq 1000$), the number of contestants.
#  $n$ lines, the $i$th of which contains the name of the contestant who places $i$th on the predicted scoreboard.
#  $n$ lines, the $i$th of which contains the name of the contestant who places $i$th on the final scoreboard.
# Each name consists of at most $100$ lower-case and upper-case alphabetical characters. All names are unique, and occur on both scoreboards exactly once.

# 출력
# If the scoreboards are suspicious, output "suspicious". Otherwise, output the name of the jury's favourite.

# 예제 입력 1 
# 3
# Plisetsky
# Katsuki
# Leroy
# Leroy
# Plisetsky
# Katsuki
# 예제 출력 1 
# Leroy
# 예제 입력 2 
# 2
# Allison
# Bobson
# Allison
# Bobson
# 예제 출력 2 
# suspicious
# 예제 입력 3 
# 3
# daSilva
# Aziz
# Peters
# Aziz
# Peters
# daSilva
# 예제 출력 3 
# Aziz

n = int(input())
predict = []
final = []

for i in range(n):
    predict += [input()]

for i in range(n):
    final += [input()]

#print(predict, final)

dif = []

for i in range(n):
    dif.append( [final.index(predict[i]) - i, final.index(predict[i]) ]   )


#print(dif)

if all (x[0] >= 0 for x in dif):
    print('suspicious')
else:
    dif.sort()
    #print(dif)
    print(final[dif[0][1]])
