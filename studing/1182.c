#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

typedef struct Graph
{
    int size;
    int *data;
    int *visited;
} Graph;

int graph_index(int a, int b)
{

    return (int)pow(2, a) - 1 + b;
}

int find(Graph *graph, int target)
{

    int temp_col = 0;
    int temp_row = 0;
    int temp_data = 0;
    int count = 0;

    int N = log2(graph->size + 1) - 1;
    int size = pow(2, N);
    int *answer = (int *)(calloc)(size, sizeof(int));

    while (1)
    {
        if (graph->visited[graph_index(temp_col, temp_row)] != 1)
        {
            temp_data += graph->data[graph_index(temp_col, temp_row)];
            graph->visited[graph_index(temp_col, temp_row)] = 1;
        }
        // 현재 위치의 visited 가 1이 아닌경우에만,
        // 현재위치의 data를 누적으로 더하고, visited를 1로 기록한다 //0, 0 은 data가 0 이므로 의미 없음
        if (temp_col == N) // 현재 위치가 leaf node인 경우
        {
            answer[temp_row] = temp_data;
        }

        if (temp_col + 1 <= N && 1 != graph->visited[graph_index(temp_col + 1, temp_row * 2)])
        {
            temp_col = temp_col + 1;
            temp_row = temp_row * 2;
        }

        else if (temp_col + 1 <= N && 1 != graph->visited[graph_index(temp_col + 1, temp_row * 2 + 1)])
        {
            temp_col = temp_col + 1;
            temp_row = temp_row * 2 + 1;
        }
        else
        {   if(temp_col == 0) break;
            temp_data -= graph->data[graph_index(temp_col, temp_row)];
            temp_col = temp_col - 1;
            temp_row = (temp_row) / 2;
        }
        // 현재 위치의 왼쪽, 오른쪽, 위 순서대로 visited 가 1 이 아닌 곳으로 이동한다.
        // 위로 움직일떄에는 현재 위치의 data를 제거하면서 올라간다.
    }

    // // 다 끝나고 나면, answer을 출력해보자
    // for (int a = 0; a < size; a++)
    // {
    //     printf("%2d ", answer[a]);
    // }
    

    for(int a = 1, answer_sum = 0; a < size; a++)
    {
        if(answer[a] == target)
            answer_sum ++;
        if(a == size -1)
            printf("%d", answer_sum);
    }
   
    return 0;
}

int main()
{
    // 첫째 줄에 정수의 개수를 나타내는 N과
    // 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000)
    // 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.
    int N, S;
    scanf("%d", &N);
    scanf("%d", &S);

    int *N_arr = (int *)malloc(sizeof(int) * N);

    for (int a = 0; a < N; a++)
    {
        scanf("%d", &(N_arr[a]));
    }

    Graph *graph = (Graph *)malloc(sizeof(Graph));
    graph->size = pow(2, N + 1) - 1;
    graph->data = (int *)malloc(sizeof(int) * (graph->size));
    graph->visited = (int *)calloc(graph->size, sizeof(int));
    graph->data[0] = 0;

    for (int col = 1, row = 0, temp = 0;; col++, temp++, row = 0)
    {
        for (; row < pow(2, col); row++)
        {
            if (row % 2 == 0)
                graph->data[graph_index(col, row)] = 0;
            else
                graph->data[graph_index(col, row)] = N_arr[temp];
        }

        if (temp == N - 1)
            break;
    }

    // for (int a = 0; a < N + 1; a++)
    // {
    //     printf("[");

    //     for (int b = 0; b < pow(2, a); b++)
    //     {

    //         printf("%2d", graph->data[graph_index(a, b)]);
    //     }

    //     printf("]\n");
    // }

    find(graph, S);
}