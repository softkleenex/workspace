#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

unsigned long long check(char a[])
{
    if(strcmp(a, "black") == 0)
        return 0;
    else if(strcmp(a, "brown") == 0)
        return 1;
    else if(strcmp(a, "red") == 0)
        return 2;
    else if(strcmp(a, "orange") == 0)
        return 3;
    else if(strcmp(a, "yellow") == 0)
        return 4;
    else if(strcmp(a, "green") == 0)
        return 5;
    else if(strcmp(a, "blue") == 0)
        return 6;
    else if(strcmp(a, "violet") == 0)
        return 7;
    else if(strcmp(a, "grey") == 0)
        return 8;
    else if(strcmp(a, "white") == 0)
        return 9;  
    return -1;        
}

    




int main()
{

unsigned long long ans = 0;    
for(int a = 0; a < 3; a++)
{

    char spell[50];
    scanf("%s", spell);
   // printf("[%lld]", check(spell));
    if(a == 0)
        ans += 10 * check(spell);
    else if(a == 1)
        ans += 1 * check(spell);
    else
        ans *= pow(10, check(spell));
}

    printf("%llu", ans);
    
return 0;    
}