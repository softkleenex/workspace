//https://www.acmicpc.net/problem/25495
//21:05~
#include<stdio.h>
#include<stdlib.h>

void check(int t, int p[])
{
    int cur = 0;
    int cur_b = 0;
    int ans = 0;
    for(int i = 0; i < t; i++)
    {
        if(cur == p[i])
            {
            cur_b = cur_b * 2;
            }
        else
            cur_b = 2;
        
        ans += cur_b;
        p[i] = ans >= 100 ? 0 : p[i];
        ans = ans >= 100 ? 0 : ans;
        cur = p[i];
    }
    printf("%d", ans);

}

int main()
{
int t = 0; scanf("%d", &t);
int* p = (int*)malloc(sizeof(int)*t);
for(int i = 0; i < t; i++)
{
    scanf("%d", &p[i]);
}

check(t, p);


return 0;
}