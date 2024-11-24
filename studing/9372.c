//https://www.acmicpc.net/problem/9372
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define even(a) a/2
#define odd(b) 3*b+1

typedef struct node{
    int data;
    node *next;
}node;


void case(int N, int M);

int main(){
int T = 0; scanf("%d", &T);

for(int i = 0 i < T; i++)
{
    int N = 0; scanf("%d",  &N);//국가
    int M = 0; scanf("%d",  &M);//비행기
    case(N. M);
}

return 0;
}


void case(int N, int M){
    node* cases = (node*)malloc(sizeof(node));




}