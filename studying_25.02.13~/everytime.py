def make_graph(n, m):
    imove = [-2, -1, 1, 2,  2,  1, -1, -2]
    jmove = [ 1,  2, 2, 1, -1, -2, -2, -1]
    graph = {i:[] for i in range(n * m)}
    for i in range(n):
        for j in range(m):
            for k in range(8):
                ni, nj = i + imove[k], j + jmove[k]
                if 0 <= ni < n and 0 <= nj < m:
                    graph[i*m + j].append(ni*m + nj)
                    
    return graph

def tour(k, v, n, m, graph, mark):
    global count
    if k == n * m:
        count += 1
        mark[v] = k
        
    else:
        for u in graph[v]:
            if mark[u] == 0:
                mark[u] = k + 1
                tour(k + 1, u, n, m, graph, mark)
                mark[u] = 0

def tour2(k, v, s, n, m, graph, mark):
    global count
    if k == n * m and s in graph[v]:
        count += 1
    else:
        for u in graph[v]:
            if mark[u] == 0:
                mark[u] = k + 1
                tour2(k + 1, u, s, n, m, graph, mark)
                mark[u] = 0



def knight_tour_count(n, m):
    global count
    graph = make_graph(n, m)
    start_node = 0
    mark = [0] * (n * m)
    mark[start_node] = 1
    count = 0
    tour2(1, start_node, start_node, n, m, graph, mark)
    return count



def main(n,m,r):
    graph = make_graph(n, m)
    
    mark = [0] * (n * m)
    mark[r]=1
    global count
    count = 0
    tour(1, r, n, m, graph, mark)
    print(count)





n, m = map(int, input().split())
count = 0
r = []

tryc  = int(input())

for i in range(tryc):
    x, y = map(int, input().split())
    r.append(m*x+y)#스타트 지점


    
result = knight_tour_count(n, m)

print(result)
for _ in r:
    main(n,m,_)
