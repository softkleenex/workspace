//https://www.acmicpc.net/problem/31797
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef struct hands{
    int hand;
    int who;
}hands;
//21:17~ 22:00
//22:10 ~ 

void sort(hands arr[], int len)
{
  
    for(int cur = 0; cur < len ; cur++)
    {
        int min = cur;
        for(int i = cur; i < len; i++)
        {   
            min = arr[i].hand > arr[min].hand ? min : i;
        }
        
        hands temp; temp.hand = arr[min].hand; temp.who = arr[min].who;
        arr[min].hand = arr[cur].hand; arr[min].who = arr[cur].who;
        arr[cur].hand = temp.hand; arr[cur].who = temp.who; 
    }//hand 기준으로 hands를 정렬한다



   for(int cur = 0; cur < len ; cur++)
   {
       // printf("[%d: %d]", arr[cur].hand, arr[cur].who);
   }




}


void search(hands *arr,int len, int t)
{
    sort(arr, len);
    int target = (t-1) % len;//

    //printf("%d %d", t, target);
   for(int cur = 0; cur < len ; cur++)
   {
       //printf("[%d: %d]", arr[cur].hand, arr[cur].who);
   }
    printf("%d", arr[target].who);

}


int main()
{

int N = 0; int M = 0; scanf("%d %d", &N, &M);
M *= 2;

hands* arr = (hands*)malloc(sizeof(hands) * M);


for(int a = 0; a < M; a++)
{
    scanf("%d", &arr[a].hand);
    arr[a].who = (a)/2 + 1;
}

for(int a = 0; a < M; a++)
{
//printf("[%d %d]", arr[a].who, arr[a].hand);
}




search(arr, M, N);

free(arr);
return 0;
}