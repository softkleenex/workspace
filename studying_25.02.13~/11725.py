# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	101736	46530	32584	43.302%
# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

# *2 + 1 , *2 + 2

n = int(input())

edges = dict()#a : parent, left, right)
for i in range(1, n+1):
    edges[i] = []

for _ in range(0, n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
#print(edges)

parents = list(0 for i in range(0, n+1))
#print(parents) #1base
stack = [(1, 0)]

while stack:
    node, parent = stack.pop()
    parents[node] = parent

    for child in edges[node]:
        if parents[child] == 0:
            stack.append((child, node))


for i in parents[2:]:
    print(i)