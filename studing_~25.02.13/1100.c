#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

int main()
{
    int arr[8][8] = {-1};
        for(int a = 0; a < 64; a++)
        {
            char temp; 
            scanf(" %c", &temp);
            if(temp == '.') *(*(arr+a/8)+ a%8) = 0;
            else *(*(arr+a/8)+ a%8) = 1;
        }
    int c = 0;
     for(int a = 0; a < 64; a++)
        {
            if(((a / 8) + (a % 8))%2 == 0)
                if(*(*(arr+a/8)+ a%8) == 1) {c++; }
        }
    printf("%d", c);



    return 0;
}