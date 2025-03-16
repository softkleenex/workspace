#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#include <string.h>

#include <stdlib.h>

int main(int argc, char* argv[])

{

	int a, b, n, w = 0;

	int ans_count = 0;
	int ans1_post = 0;
	int ans2_post = 0;
	int left = 1;
	int right = 1000;


	if (0 == scanf("%d %d %d %d", &a, &b, &n, &w))
		return 0;
	//w = 양 * a + (n - 양)b, a == b = c라면? w = 양 * c + (n-양)*c = n*c.양의 값에 상관없이 w == n*c라면 항상 참이다. 양 == 1, n-1 염소 == 1 이 아니라면? -1

	if (a == b)
	{
		if (n == 2 && a * 1 + b * 1 == w)
		{
			printf("%d %d", 1, 1);
			return 0;
		}
		else
		{
			printf("%d", -1);
			return 0;
		}

	}
	//w = 양 * a + (n - 양)b, a != b 라면? w = 양 * a + (n-양)*b, w == 양 * a - 양 * b + n*b 
	else
		for(int ans1 = 1; ans1 <= 1000; ans1++)
        {
            int cal = a*ans1 + b*(n - ans1);
            ans1 = ans1; 
            int ans2 = n - ans1;
            if(cal == w && ((1 <= ans1 && ans1 <= 1000) && (1 <= ans2 && ans2 <= 1000)))
            {
                ans_count++;
                ans1_post = ans1;
                ans2_post = ans2;
            }
        }

if(ans_count == 1)
{
    printf("%d %d", ans1_post, ans2_post);
}
else
{
printf("%d", -1);

}

	return 0;

}