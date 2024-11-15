//2021111470 이상재
//1번은 결과가 동일해야하고
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define fn "D:\\my_note2_openthis\\school\\24.11.13\\in.txt"
//#define fn "in.txt"


typedef struct node{
    int data;
    struct node* next;
}node;

typedef struct graph{
    struct node* graph_list;
}graph;

void init_node(node *temp, int c){
    temp->next = NULL;
    temp->data = c;
}


void init_graph(graph temp, int c)
{
    for(int i = 0; i < c; i++)
        init_node(&(temp.graph_list[i]), c);
}


void direct_p_g_list(graph* graphs, int vx);
void p_degree(graph *graphs, int vx);
void d_g_list();
void free_g(graph* graphs, int vx);

void in_graph(node* start, int t)
{
    node* in = (node*)malloc(sizeof(node));
    init_node(in, t);
    node* NEXT = start->next;
    start->next = in;

    if(NEXT != NULL)
        {
            in->next = NEXT;
        }
}

void free_g(graph* graphs, int vx)
{//정, 역방향 그래프를 번갈아 가기 떄문에 print g에서 free시도시에 역방향은 free됨, 정방향은 print g를 하지 않아 free 함수 별도
    for(int i = 0; i < vx; i++)
    {
        node* temp = graphs->graph_list[i].next;
        while(temp != NULL)
            {
                node* free_temp = temp;
                temp = temp->next; 
                free(free_temp);
            }
    }
}




void p_degree(graph *graphs, int vx)
{//print g에서 약간만 변형함, in or out인지는 이 함수 호출전 기재
    for(int i = 0; i < vx; i++)
    {
        printf("[%d]  ", i);
        int count = 0;
        node* temp = graphs->graph_list[i].next;
        while(temp != NULL)
            {
                count++;
                temp = temp->next; 
            }
        printf("%d\n", count);
    }
}


void p_g_list(graph* graphs, int vx)
{
    printf("\nLinked adjacency list\n");
    for(int i = 0; i < vx; i++)
    {
        printf("[%d]  ", i);
        node* temp = graphs->graph_list[i].next;
        while(temp != NULL)
            {
                printf("%d  ", temp->data);
                temp = temp->next;
            }
        printf("\n");
    }
}

void inverse_g_list(){//1.c의 list로 g 만드는것 이용, 단순 fscanf의 변수 뒤집음
FILE *fp1 = fopen(fn, "r"); if(fp1 == NULL) printf("!file error!");
int vx = 0; fscanf(fp1, "%d", &vx);
graph graphs;
graphs.graph_list = (node*)malloc(sizeof(node) * vx);
init_graph(graphs, vx);

int e = 0; fscanf(fp1, "%d",  &e);
for(int i = 0; i < e; i++)
{
    int s = 0; int t = 0; fscanf(fp1, "%d %d", &t, &s);
    in_graph(&graphs.graph_list[s], t);
}

p_g_list(&graphs, vx);

printf("Indegree\n");
p_degree(&graphs, vx);


d_g_list();

free_g(&graphs, vx);
fclose(fp1);
}




void d_g_list(){//정방향 g도 별도 구현
FILE *fp1 = fopen(fn, "r"); if(fp1 == NULL) printf("!file error!");
int vx = 0; fscanf(fp1, "%d", &vx);
graph graphs;
graphs.graph_list = (node*)malloc(sizeof(node) * vx);
init_graph(graphs, vx);

int e = 0; fscanf(fp1, "%d",  &e);
for(int i = 0; i < e; i++)
{
    int s = 0; int t = 0; fscanf(fp1, "%d %d", &s, &t);
    in_graph(&graphs.graph_list[s], t);
}

printf("Outdegree\n");
p_degree(&graphs, vx);

free_g(&graphs, vx);

fclose(fp1);
}





int main()
{
inverse_g_list();


return 0;
}