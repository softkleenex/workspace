// https://www.acmicpc.net/board/view/160360

#include <stdio.h>


int main(void)
{
	int t, k, n, i, j, p, apa[15][15] = {0};
	scanf("%d", &t);
	for(i = 0; i < 14; i++)
	{
		apa[0][i] = i + 1;
		apa[i][0] = 1;
	}

    apa[14][0] = 1;

	for(i = 0; i < t; i++)
	{
		scanf("%d %d", &k, &n);
		for(j = 1; j <= k; j++)
		{
			for(p = 1; p < n; p++)
			{
				apa[j][p] = apa[j][p - 1] + apa[j - 1][p];
			}
		}
		printf("%d\n", apa[k][n - 1]);
	}
	return 0;
}