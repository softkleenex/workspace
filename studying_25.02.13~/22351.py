def is_valid_sequence(a, s):
    b = a
    temp = ''


    while len(temp) < len(s):
        temp += str(b)
        b += 1


        
    if temp == s:
        return True, b - 1
    return False, -1





s = input().strip()
answer = None





for alen in range(1, 4): 
    a = int(s[:alen])
    valid, b = is_valid_sequence(a, s)
    if valid:
        if answer is None or a < answer[0]: 
            answer = (a, b)






print(answer[0], answer[1])