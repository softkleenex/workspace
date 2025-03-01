#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>



int arrsum(int arr[], int length)
{
    int sum = 0;
    for(int a = 0; a < length; a++)
    {
        sum += arr[a];
    }

    return sum;
}
//프림 알고리즘의 종료 시점의 지표
//visited의 총 sum이 V*1이되면 종료

int main()
{   
  
    int V;
    int E;
    scanf("%d %d", &V, &E);
    int **graph = (int **)malloc(sizeof(int) * V);
 
    for (int a = 0; a < V; a++)
    {
        graph[a] = (int *)malloc(sizeof(int) * E);
    }
    for (int a = 0; a < V; a++)
    {
        for (int b = 0; b < V; b++)
        {
            graph[a][b] = INT_MAX;
        }
    }

    for (int a = 0; a < E; a++)
    {
        int x, y, z;
        scanf("%d %d %d", &x, &y, &z);
        graph[x-1][y-1] = z;
        graph[y-1][x-1] = z;
    }

/*{
    printf("   ");
    for(int b= 0; b < V; b++)    
    {
        printf(" %d ", b);
    }
    printf("\n");
    for (int a = 0; a < V; a++)
    {  
     
        printf("%d |", a);
        for (int b = 0; b < V; b++)
        {
            if(graph[a][b] == INT_MAX)
                printf(" 0 ");
            else
                printf(" %d ",graph[a][b]);
        } 
    printf("\n");
    }
}*/
//가중치 저장된 graph 함수 출력





//start 프림 알고리즘 구현!

int weight = 0;
int* visit = (int*)malloc(sizeof(int) * V);

for(int a = 0; a < V; a++){
    visit[a] = 0;
}
visit[0] = 1;

 //제일 처음 시작(temp_V의 초기값은 0)
 //> no visit, 1 > visit, > ture면 vist, false면 novisit

while(arrsum(visit, V) != V*1){  
 
    int s_index = 0;
    int t_index = 0;
    // 각각 시작인덱스, 타겟인덱스를 가르킨다
    // min을 정하면서, 그 edge를 정보를 담는용도

  

    for(int a = 0, min = INT_MAX; a < V; a++){
    if(visit[a]){//방문한 V에 대해서만
            for(int b = 0; b <V; b++)
            {
            if(!(visit[b]) && //미방문 v에 대해서만
                min > graph[a][b] && graph[a][b] != INT_MAX)
                {
                    s_index = a;
                    t_index = b;
                    min = graph[a][b];
                }  
            }
        }
    }
    //방문한 v > 미방문 v의 간선들에 대해서만 min을 골라내었다
    //해당 v에서 가장 가중치가 낮은 간선을 골랐다, 그 값은 graph[temp_V][index]
    
    if(!visit[t_index])//선택한 간선이 연결한 정점이 방문된적 없다면
    {
        visit[t_index] = 1;
        weight += graph[s_index][t_index];//그 간선은 최소 스패닝 트리에 연결된다
    }
    
}

/*
1 임의의 정점을 선택하여 하나의 정점을 갖는 최초의 트리를 구성한다.
2 트리에 포함된 정점과 트리에 포함되지 않은 정점 간의 간선 중
가장 작은 가중치를 가지는 간선을 선택하여 트리에 추가한다.
3 모든 정점이 트리에 포함될 때 까지 2를 반복한다.*/




//프림 알고리즘 구현!

printf("%d", weight);

return 0;

} 