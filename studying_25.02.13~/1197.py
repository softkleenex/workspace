# 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

# 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

# 입력
# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

# 그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

# 출력
# 첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.


import sys
input = sys.stdin.readline


#대표 값을 찾는 함수
# def find(link, x):
#     while link[x] != x:
#         link[x] = link[link[x]]

#     return link[x]

def find(link, x):
    while link[x] != x:
        link[x] = link[link[x]]
        x = link[x]

    return link[x]

#두 무리를 묶는 함수, 경로 압축되었으므로 사이즈 비교는 필요 없다
def unite(link, x, y):
    x = find(link, x)
    y = find(link, y) 
    link[y] = x
    #같은무리 > 같은 객체 참조, 어떤 무리의 하나의 대푯값만 변경하도 같은 무리의 대푯값도 변경된다!

v, e = map(int, input().split())
edges = []

for i in range(0, e):
    a, b, c = map(int, input().split())
    s = (c, a-1, b-1)
    edges.append(s)


edges.sort()
link = [i for i in range(0, v)]


used_edges = []
sum_cost = 0

while len(used_edges) !=  v -1:
    cost, a, b = edges.pop(0)
    if find(link, a) != find(link, b):
        unite(link, a, b)
        sum_cost += cost
        used_edges.append([cost, a, b])
    else:
        continue

print(sum_cost)