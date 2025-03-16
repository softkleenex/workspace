//2021111470 이상재
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#define file_name "D:\\my_note2_openthis\\school\\24.11.20\\in.txt"
#define file_name "in.txt"
//20:10 ~ 20:57 21:13~21:53


void search(int count_node, int** graph, int start)
{
    int** graph2 = (int**)calloc(count_node, sizeof(int*));//prim 알고리즘 용 graph와 같은 size graph2
    for(int i = 0; i < count_node; i++)
    {
        graph2[i] = (int*)calloc(count_node, sizeof(int));
    }
    graph2[start][start] = 1;//시작 노드는 방문으로 시작



    while(1)
    {
        int start_node = 0;
        int target_node = 0;
        int min = 9999;//방문 여부, 기준을 정하는 변수들

        for(int s = 0; s < count_node; s++)//시작 노드 탐색
            {
                if(graph2[s][s] == 1)//해당 노드 방문되었다면? 다음으로
                {
                    for(int t = 0; t < count_node; t++)//도착 노드 탐색
                    {
                        if(s != t && graph[s][t] != 0 && graph2[t][t] == 0 && graph[s][t] < min)//해당 노드가 다른 노드와 연결되어 있고, 방문된 간선이 아니라면
                        {//조건에 맞다면, 변수들 업데이트
                            min = graph[s][t];
                            start_node = s;
                            target_node = t;
                        }               
                    }
                }    
            }
        if(min == 9999) break;//min이 업데이트 되지 않았다면 종료
        
        if(start_node != target_node) printf("(%d %d)\n", start_node, target_node);//출발, 도착 노드 print
        graph2[target_node][target_node] =  1;//방문 노드 반영
        graph2[start_node][target_node] = min;
        graph2[target_node][start_node] = min;

        int sum = 0;
        for(int i = 0; i < count_node; i++) sum += graph2[i][i];//모든 node방문시 종료
        if(sum == count_node) break;
         
    }


for(int i = 0; i < count_node; i++) {free(graph2[i]);}
free(graph2);
}

     
int main()
{
FILE* fp1 = NULL;
fp1 =  fopen(file_name, "r");
if(fp1 == NULL) {printf("file error"); return 1;}
int count_node = 0; fscanf(fp1, "%d", &count_node);
int** graph = (int**)calloc(count_node, sizeof(int*));

for(int i = 0; i < count_node; i++)
{
    graph[i] = (int*)calloc(count_node, sizeof(int));
}

int count_edge = 0; fscanf(fp1, "%d", &count_edge);

for(int i = 0; i < count_edge; i++)
{
    int start = 0; int target = 0; int weight = 0;
    fscanf(fp1, "%d %d %d", &start,  &target, &weight);
    graph[start][target] = weight;
    graph[target][start] = weight;
}

int start = 0;
printf("Input start node: "); scanf("%d", &start);
search(count_node, graph, start);






for(int i = 0; i < count_node; i++) {free(graph[i]);}
free(graph);

fclose(fp1);
return 0;
}