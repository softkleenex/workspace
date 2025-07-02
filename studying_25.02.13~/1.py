n , m = map(int, input().split())

basket = [z for z in range(1,n+1)]

for _ in range(m) :
    i , j = map(int, input().split())
    
    count = int(len(basket[i:j+1])/2)

    
    for _ in range(count) :
        basket[i-1], basket[j-1] = basket[j-1],basket[i-1]
        i += 1
        j -= 1


print(*basket)