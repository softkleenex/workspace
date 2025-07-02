import sys
input = sys.stdin.readline

a = int(input())
input1 = reversed(input())


while (input1 != '' and input1.replace('HHOOHH', '') != input1):
    input1 = input1.replace("HHOOHH", '')

while (input1 != '' and input1.replace('HOHOHH', '') != input1):
    input1 = input1.replace("HOHOHH", '')


while (input1 != '' and input1.replace('HOH', '') != input1):
    input1 = input1.replace("HOH", '')
    

if len(input1) == 0 or input == 'HHOOHH' or input == 'HOHOHH':
    print('pure')

else:
    print('mix')