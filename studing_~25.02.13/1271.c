#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
unsigned long long n, m;

scanf("%llu %llu", &n, &m);    
printf("%llu\n%llu", n/m, n%m);

    return 0;
}