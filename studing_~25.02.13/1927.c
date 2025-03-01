#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#define swap(a, b) do{int temp = a; a = b; b = temp;}while(0)

int heap[100000];
int size = 0;



int parent(int index)
{ 
    return (index -1) /2;
}

int leftChild(int index)
{ 
    return (index)*2 +1;
}

int rightChild(int index)
{ 
    return (index)*2 + 2;
}


void insert(int value)
{
    if (size == 9999)
    {}    //힙이 꽉 찼다
    
    int index = size;
    heap[size] = value;
    size ++;
    
    while ((index != 0) && (heap[parent(index)] > heap[index]))
    {
        swap(heap[index], heap[parent(index)]);
        index = parent(index);
    }
}




void minHeapify(int index)
{
    int left = leftChild(index);
    int right = rightChild(index);
    int smallest = index;

    if (left < size && heap[left] < heap[smallest])
        smallest = left;
    if(right < size && heap[right] < heap[smallest])
        smallest = right;
    
    if (smallest != index)
    { 
        swap(heap[index], heap[smallest]);
        minHeapify(smallest);
    }

}

int removeMin()
{
    if (size <= 0)
        return 0;
    
    if (size == 1)
    {
        size -= 1;
        return heap[0];
    }

    int root = heap[0];
    heap[0] = heap[size -1];
    size -= 1;
    minHeapify(0);

    return root;

}




int main()
{
int n = 0;
scanf("%d", &n);



int* arr2 = (int*)malloc(sizeof(int) * (size_t)n);

for(int a = 0; a < n; a ++)
{
    scanf("%d", &arr2[a]);
}

for(int a = 0; a < n; a++)
{
int x = 0;
x = arr2[a]; 
//0 입력시 배열의 최소값 출럭, 그 배열 제거 
// 자연수 입력시에 배열에 그 값 넣음

    if(x == 0)
    {
        if(size == 0) //인덱스가 0 >> 즉, 배열이 아예 비워져 있는 경우
            printf("0\n");
        else//배열에 뭐라도 있는 경우
        {   
            printf("%d\n", heap[0]);
            removeMin();
        }
    }
    if(x > 0)
    {
       insert(x);
    }
}


return 0;

}