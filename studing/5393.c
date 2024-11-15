//https://www.acmicpc.net/problem/5393
//19:33~20:31
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define even(a) a/2
#define odd(b) 3*b+1







void hole_list(unsigned long long hole)
{

  unsigned long long even = hole/2 + hole % 2;
  hole++;
  unsigned long long odd = hole/6 + hole %3;
  
  //10> 7 14/ 8 16/ 9 18 / 10 20 / 11 22/ 12 24 // 5 16/ 7 22/ 9 28 / 11 34 


  //5 > 3 6/ 4 8 / 5 10// 3 10 / 5 16


  printf("%llu %llu", even, odd);

 // printf("%llu", even+odd);
}


int main()
{
    int t = 0; scanf("%d", &t);
    
    for(int a = 0; a < t; a++)
    {
    unsigned long long int hole = 0; scanf("%llu", &hole);
    hole_list(hole);
    if(a < t-1)printf("\n");    
    }
    
return 0;

    }