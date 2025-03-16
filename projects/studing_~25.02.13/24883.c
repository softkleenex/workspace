#include<stdio.h>
#include<string.h>

int main(){
    char N = '0'; scanf("%c", &N);
    if(N == 'N' || N == 'n')
        printf("Naver D2");
    else
        printf("Naver Whale");


    return 0;
}