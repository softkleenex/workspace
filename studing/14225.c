#include <stdio.h>
#include <stdlib.h>



//https://www.acmicpc.net/problem/18511


int ans(int klen, int k[], int N)
{
	int tempmax = 0;
	int max = 0;
	
	for(int a = 0; a <klen; a++)
	{
		for(int b = 0; b <klen; b++)
			for(int c = 0; c <klen; c++)
				{
				if((k[a] != 0 && (k[b] != 0 && k[c] != 0)) || (k[b] != 0  && (k[c] != 0)))
				{
				tempmax = 100 * k[a] +10 * k[b] +1 * k[c];
				}
				if(tempmax <= N && tempmax > max) {max = tempmax;}  tempmax = 0;	
				//조건이 맞는다면 max갱신, tempmax는 무조건 초기화
				}
	}
	return max;	
}
	


int main(int argc, char *argv[])
{
	int N = 0; 
	int klen = 0 ; int k[4] = {0};
	
	scanf("%d", &N);
	scanf("%d", &klen);
	
	for(int a  = 0; a < klen; a++)
	{
		scanf("%d", &k[a]);
		}
		
	
	
	klen++;
	
	
	for(int a  = 0; a < klen; a++)
	{
	//printf("%d / ", k[a]);
		}
	
	
	printf("%d" , ans(klen, k, N));
	
	
	
		
			return 0;	
}