#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#define min(a, b) ((a) < (b) ? (a) : (b))
#define max(a, b) ((a) > (b) ? (a) : (b))

//gcd - 최대공약수 - 하나는 모듈러 연산 써서, 하나는 모듈러 연산 없이 답 - 7425


int module(int a, int b){
    int temp = 1;
    int answer = 0;

    while(temp < min(a,b )){
        if(a % temp == 0 && b % temp == 0)
            answer = temp;
        temp ++;
    }

    return answer;
}

int nonmodule(int a, int b)
{
    if(b == 0)
        return a;
    while(a >= b)
     a -= b;

     nonmodule(a, b);
     return 0;
}

int main(){
    int a = 7276500;
    int b = 3185325;

    printf("by module - %d\n", module(a, b));

    printf("by nonmodule - %d\n", module(a, b));


    return 0;
}