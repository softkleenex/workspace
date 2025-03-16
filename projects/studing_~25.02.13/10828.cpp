#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

// 스택 구조체 정의
typedef struct
{
    int *data; // 스택 데이터를 저장할 배열
    int top;   // 스택의 최상위 원소의 인덱스
} stack;

stack *init()
{
    stack *stacks = (stack *)malloc(sizeof(stack));
    stacks->data = (int *)calloc(10000, sizeof(int));
    stacks->top = -1;
    return stacks;
}

// 정수 X를 스택에 넣는 연산이다.
void push(stack *stacks, int x)
{
    stacks->data[stacks->top + 1] = x;
    (stacks->top)++;
}

// 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
// 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void pop(stack *stacks)
{
    if (stacks->top != -1)
    {
        printf("%d\n", stacks->data[stacks->top]);
        stacks->data[stacks->top] = -1;
        stacks->top--;
    }
    else
        printf("-1\n");
}

// 스택에 들어있는 정수의 개수를 출력한다.
void size(stack *stacks)
{
    printf("%d\n", stacks->top + 1);
}

// 스택이 비어있으면 1, 아니y면 0을 출력한다.
void empty(stack *stacks)
{
    if (stacks->top != -1)
        printf("0\n");
    else
        printf("1\n");
}

// 스택의 가장 위에 있는 정수를 출력한다.
// 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void top(stack *stacks)
{
    if (stacks->top != -1)
        printf("%d\n", stacks->data[stacks->top]);
    else
        printf("%d\n", -1);
}

int main()
{

    int N = 0;

    stack *stacks = init();

    scanf("%d", &N);

    int command[10000] = {-1};
    int push_arr[10000] = {-1};
    int push_count = 0;

    for (int a = 0; a < N; a++)
    {
        char temp1[10];
        scanf("%s", temp1);

        if (0 == strncmp(temp1, "push", 4))
        {
            command[a] = 0;
            scanf("%d", &push_arr[push_count]);
            push_count++;
        }
        else if (0 == strncmp(temp1, "pop", 3))
        {
            command[a] = 1;
        }
        else if (0 == strncmp(temp1, "size", 4))
        {
            command[a] = 2;
        }
        else if (0 == strncmp(temp1, "empty", 5))
        {
            command[a] = 3;
        }
        else if (0 == strncmp(temp1, "top", 3))
        {
            command[a] = 4;
        }
    }
    push_count = 0;
    for (int a = 0; a < N; a++)
    {

        switch (command[a])
        {
        case (0):
        {
            push(stacks, push_arr[push_count]);
            push_count++;
            break;
        }
        case (1):
        {
            pop(stacks);
            break;
        }
        case (2):
        {
            size(stacks);
            break;
        }
        case (3):
        {
            empty(stacks);
            break;
        }
        case (4):
        {
            top(stacks);
            break;
        }
        default:
        {

            break;
        }
        }
    }
}