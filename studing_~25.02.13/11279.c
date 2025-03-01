#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int main(){
    int N = 0;
    scanf("%d", &N);

    int arr[100000] = {};
    for(int a = 0; a < N; a++)
    {
        int x = 0;
        scanf("%d", &x);
        if(x != 0) // x가 자연수라면 
                    //배열에 x라는 값을 넣는(추가하는) 연산이고
        {

        }
        else{ // x가 0이라면 배열에서 가장 큰 값을 출력하고 
                //그 값을 배열에서 제거하는 경우이다
                // 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 
                    //한 경우에는 0을 출력하면 된다.


        }
    }
}