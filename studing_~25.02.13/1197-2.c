#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

typedef struct
{
    int v1;
    int v2;
    int w;
} edge;


//병합함수 > 쪼개진 배열을 하나로 합침
void merge(edge *edgearr[], int l, int m, int r){

int n1 = m -l + 1;
int n2 = r-m;

edge** Ledge = (edge**)malloc(sizeof(edge*) * n1);


for(int a = l; a < m; a++)
{
    Ledge[a] -> v1 = edgearr[a] -> v1;
    Ledge[a] -> v2 = edgearr[a] -> v2;
    Ledge[a] -> w = edgearr[a] -> w;
}

edge** Redge = (edge**)malloc(sizeof(edge*) *  n2);

for(int a = m; a <= r; a++)
{
   Ledge[a] -> v1 = edgearr[a] -> v1;
   Ledge[a] -> v2 = edgearr[a] -> v2;
   Ledge[a] -> w = edgearr[a] -> w;
}




}

void mergesort(edge *edgearr[], int l, int r){
        if (l < r){
            int m = l + (r-1)/2;
            mergesort(edgearr, l, m);
            mergesort(edgearr, m+1, l);

            merge(edgearr, l, m, r);
        }


}




int main()
{

    int V, E;

    scanf("%d %d", &V, &E);

    edge **edgearr1 = (edge **)malloc(sizeof(edge *) * E);
    // edge 포인터 배열을 동적할당 했다

    for (int a = 0; a < E; a++)
    {
        int q, w, e;
        scanf("%d %d %d", &q, &w, &e);

        if (q < e)
        {
            edgearr1[a]->v1 = q;
            edgearr1[a]->v2 = w;
        }
        if (e < q)
        {
            edgearr1[a]->v1 = w;
            edgearr1[a]->v2 = q;
        }
        edgearr1[a]->w = E;
    }


//병합정렬을 통해 edge를 weight를 기준으로 작은것 부터 배치한다.

  edge **edgearr2 = (edge **)malloc(sizeof(edge *) * E); //병합정렬의 결과를 넣을 배열
  
  





    // 1 임의의 정점을 선택하여 하나의 정점을 갖는 최초의 트리를 구성한다.
    // 2 트리에 포함된 정점과 트리에 포함되지 않은 정점 간의 간선 중
    // 가장 작은 가중치를 가지는 간선을 선택하여 트리에 추가한다.
    // 3 모든 정점이 트리에 포함될 때 까지 2를 반복한다.*/

    // 프림 알고리즘 구현!

    return 0;
}