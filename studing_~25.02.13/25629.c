//https://www.acmicpc.net/problem/25629
//20:43~21:04
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define data(a) a%2 == 0

void check(int arr[], int len)
{//1. arr을 정렬한다. 
//2.len이 홀수라면, arr은 홀수가 (len)/2 +1, 짝수가 len/2
//3.짝이면, 홀수가 len/2, len/2개여야 한다.
//4. 정렬은 필요없고, arr에서 홀, 짝의 개수만 세자


int odd = 0; int even = 0;
    for(int i = 0; i < len; i++)
    {
    if(data(arr[i]) == 0)
        odd++;
    else even ++;
    }

//printf("[%d %d]", odd, even);

switch(data(len))
    {
    case(0)://홀인 경우
    {
        if(odd == (len) / 2 + 1 && even == (len) / 2)
        {
            printf("1");
        }        
        else
            printf("0");
        break;
    }
    default://짝인 경우
    {
        if(odd == (len) / 2 && even == (len) / 2)
        {
            printf("1");
        }          
        else
            printf("0");
    }
    }

}


int main()
{
    int len = 0; scanf("%d", &len);
    int *arr = (int*)malloc(sizeof(int)*len);
    for(int a = 0; a < len; a++)
    {
        scanf("%d", &arr[a]);
    }

    check(arr, len);


    return 0;
}