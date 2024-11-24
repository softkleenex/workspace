//https://www.acmicpc.net/problem/1058
//11:12 12:25~
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef struct node{
	int data;
	struct node* next;
}node;

typedef struct graph{
	node *nodes_1;
	node *nodes_2;
	}graph;

void init_n(node* temp, int d)
{
	temp->data = d; temp->next =NULL;
}

void init_g(graph *temp, int d)
{
	temp->nodes_1 = (node*)malloc(sizeof(node));
	temp->nodes_2 = (node*)malloc(sizeof(node));
	init_n(temp->nodes_1, d);
	init_n(temp->nodes_2, d);	
}


	
	
void push_f(graph *temp, int target)
{
	node* NEXT = temp->nodes_1->next;
	node* next_f = (node*)malloc(sizeof(node));
	init_n(next_f, target);
	temp->nodes_1->next = next_f;
	if(NEXT != NULL)
	{
		temp->nodes_1 -> next -> next = NEXT;
		}
}

void add_f1nd(graph *temp, int t)
{
	char* arr = (char*)malloc((t+1) * sizeof(char));
	scanf("%s", arr);
	for(int i = 0; i < t; i++)
		{
			if(arr[i] == 'Y')
				{
					push_f(temp, i);
			}
	}
	free(arr);
}


void add_f2nd(graph **temp, int t)
{
	node* cur =  temp[t]->nodes_2->next;
	while(cur != NULL)
	{
		node* cur_2 = temp[cur->data]->nodes_2->next;//temp[t]의 친구의 친구를 가르키고 있다
		while(cur_2 != NULL)
		{	
			node* temp = (node*)malloc(sizeof(node));
						

			cur_2 = cur_2 -> next;
		}	
	}



}


void check_f(graph* temp)
{
	int count = 0;
	node* cur = temp->nodes_1;	
	while(1)
	{
		if(cur->next != NULL)
			{
				cur = cur->next;
				count++;
				}
			else break;
		}
		printf("%d\n", count);	
}







int main(int argc, char *argv[])
{
	int t = 0; scanf("%d", &t);
	
	graph** friends = (graph**)malloc(sizeof(graph)*t);
	
	for(int i = 0; i < t; i++)
	{
		friends[i] = (graph*)malloc(sizeof(graph));
		init_g(friends[i], i);
		}
	for(int i = 0; i < t; i++)
	{
		add_f1nd(friends[i], t);
		}
	
	
	
	for(int i = 0; i < t; i++)
	{
		add_f2nd(friends[i], t);
		}
	
	for(int i = 0; i < t; i++)
	{
		check_f(friends[i]);
	}
	
	
	
	
	
	
	
	free(friends);
	return 0;
}