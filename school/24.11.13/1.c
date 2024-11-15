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

void in_graph(node* start, int t)
{//+ edge
    node* in = (node*)malloc(sizeof(node));
    init_node(in, t);
    node* NEXT = start->next;
    start->next = in;

    if(NEXT != NULL)
        {
            in->next = NEXT;
        }


}


void p_g_list(graph* graphs, int vx)
{//printf graph as list
    printf("\nLinked adjacency list\n");
    for(int i = 0; i < vx; i++)
    {
        printf("[%d]  ", i);
        node* temp = graphs->graph_list[i].next;
        while(temp != NULL)
            {
                printf("%d  ", temp->data);
                node* free_temp = temp;
                temp = temp->next; free(free_temp);
            }
        printf("\n");
    }
}

void g_list(){//make graph as linked list
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

p_g_list(&graphs, vx);


fclose(fp1);
}



void g_matrix()
{//make g as matrix
FILE *fp1 = fopen(fn, "r"); if(fp1 == NULL) printf("!file error!");
int vx = 0; fscanf(fp1, "%d", &vx);
int** g = (int**)calloc((vx), sizeof(int*));
for(int a = 0; a < (vx); a++)
{
    g[a] = (int*)calloc((vx), sizeof(int));
}

int eg = 0; 
fscanf(fp1, "%d",  &eg);

for(int a = 0; a <eg; a++)
{
    int s = 0; int t = 0; fscanf(fp1, "%d %d",  &s,  &t);
    g[s][t] = 1;
}


 printf("Adjacency matrix\n");

    for(int a = 0; a < vx; a++)
    {
        for(int i = 0; i < vx; i++)
             printf("%d ", g[a][i]);
        free(g[a]);
        printf("\n");
    }

free(g);
fclose(fp1);
}



int main()
{
g_matrix();


g_list();
return 0;
}