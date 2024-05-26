#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

struct stack
{
    struct stack *prev;
    int data;
    struct stack *next;
};

typedef struct stack stack;

void init(stack *stack)
{
    if (stack != NULL)
    {
        stack->prev = NULL;
        stack->data = 0;
        stack->next = NULL;
    }
}

stack *head(stack *stacks)
{
    stack *temp1 = stacks;
    if (temp1 != NULL)
    {
        while (temp1->prev != NULL)
        {
            temp1 = temp1->prev;
        }
    }
    return temp1;
}

stack *tail(stack *stacks)
{
    stack *temp1 = stacks;
    if (temp1 != NULL)
    {
        while (temp1->next != NULL)
        {
            temp1 = temp1->next;
        }
    }
    return temp1;
}

int pushx(stack *stacks, int x)
{
    if (stacks != NULL)
    {
        stack *temp1 = (stack *)malloc(sizeof(stack));
        init(temp1);
        temp1->prev = tail(stacks);
        tail(stacks)->next = temp1;
        temp1->data = x;
    }
    
    else if (stacks == NULL)
    {
        stack *temp1 = (stack *)malloc(sizeof(stack));
        init(temp1);
        temp1->data = x;
        stacks = temp1;
    }
    
    return 0;
}
// 정수 X를 스택에 넣는 연산이다.

int pop(stack *stacks)
{
    if (stacks != NULL)
    {
        printf("%d\n", tail(stacks)->data);
        stack *temp1 = tail(stacks);
        temp1->prev->next = NULL;
        init(temp1);
        free(temp1);
    }
    else
    {
        printf("-1\n");
    }
    return 0;
}
// 스택에서 가장 위에 있는 정수를 빼고,
// 그 수를 출력한다. 만약 스택에
// 들어있는 정수가 없는 경우에는 -1을 출력한다.

int size(stack *stacks)
{
    if (stacks == NULL)
    {
        printf("0\n");
        return 0;
    }
    else
    {
        int count = 1;
        stack *temp1 = (stack *)malloc(sizeof(stack));
        temp1 = head(stacks);

        while (1)
        {
            if (temp1->next == NULL)
                break;
            else
            {
                temp1 = temp1->next;
                count++;
            }
        }

        printf("%d", count);

        return 0;
    }
}
// 스택에 들어있는 정수의 개수를 출력한다.
int empty(stack *stacks)
{
    if (stacks == NULL)
    {
        printf("1\n");
    }
    else
        printf("0\n");

    return 0;
}

// 스택이 비어있으면 1, 아니면 0을 출력한다.
int top(stack *stacks)
{
    if (head(stacks) == NULL)
        printf("-1\n");
    else
        printf("%d", tail(stacks)->data);

    return 0;
}
// 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

int main()
{
    // 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
    // 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
    // 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.
    //  문제에 나와있지 않은 명령이 주어지는 경우는 없다.

    int N;
    scanf("%d", &N);

    stack *stacks = NULL;

    for (int a = 0; a < N; a++)
    {
        char command[10] = {};
        scanf("%s", command);

        if (0 == strcmp(command, "push"))
        {
            int x;
            scanf("%d", &x);
            pushx(stacks, x);
        }
        else if (0 == strcmp(command, "pop"))
        {
            pop(stacks);
        }
        else if (0 == strcmp(command, "size"))
        {
            size(stacks);
        }
        else if (0 == strcmp(command, "empty"))
        {
            empty(stacks);
        }
        else if (0 == strcmp(command, "top"))
        {
            top(stacks);
        }
    }

    return 0;
}