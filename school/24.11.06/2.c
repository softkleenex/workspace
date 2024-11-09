//2021111470 이상재
#define file_n "in.txt"
//#define file_n "D:\\my_note2_openthis\\school\\24.11.06\\in.txt"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define l(index) index*2+1
#define r(index) index*2+2
#define p(index) (index-1)/2
#define swap(a, b) {int c = a; a = b; b = c;}
//start 11.07 17:55~ 18:43, 18:55~19:20
//1 minheap 구현후 level order traversal, 2 K입력받고 1~K번쨰 작은거 출력, << heap delection

void print_heap(int heap[], int end);
void heap_delectioned(int heap[], int end);

void min_heap(int heap[], int end)
{//올라가면 내려갈 일이 없으니...
  int cur = end;
  while(1)
  {
    int tar = p(cur);
    if(heap[cur] >= heap[tar])
    {
      break;
    }
    
    else
    {
      swap(heap[cur], heap[tar]);
      cur = tar;
    }
  }
}

void print_heap(int heap[], int end)
{
  for(int a = 0; a <= end; a++)
  {
    printf("%d ", heap[a]);
  }
  printf("\n");
}

void heap_deletion(int heap[], int* end)
{
  printf("%d ", heap[0]);
  heap[0] = heap[*end];
  heap[*end] = -1; (*end)--;
  heap_delectioned(heap, *end);
}

void heap_delectioned(int heap[], int end)
{//삭제된후, 가장 끝 data가 heap[0]인 상태
  int cur = 0;
  while(1)
  {
    if(l(cur) > end || r(cur) > end)
    {//둘중에 하나라도 벗어났으면
      break;//종료
    }
    else
    {
      int min = heap[l(cur)] <= heap[r(cur)] ? l(cur) : r(cur);
      if(heap[cur] > heap[min])
      {
        swap(heap[cur], heap[min]);
        cur = min;
      }
      else
      {
        break;
      }
    }
  }
  //r이 유효하면 > l도 유효, 즉, l만 유효한것만 예외 처리
  if(l(cur) <= end)
  {
      int min = l(cur);
      if(heap[cur] > heap[min])
      {
        swap(heap[cur], heap[min]);
        cur = min;
      }
  }

}  
int main()
{
    FILE *fp; fp = fopen(file_n, "r"); 
    if(fp == NULL) {printf("file error"); exit(0);} 
    int try_count = 0; 
    fscanf(fp, "%d", &try_count);
    //printf("%d\n", try_count);
    

    int* arr; 
    arr = (int*)malloc(sizeof(int)*try_count);
    int end = -1;


    for(int a = 0; a < try_count; a++)
    {
      end++;
      fscanf(fp, "%d", &arr[end]);
      min_heap(arr, end);
     // print_heap(arr, end);
    }
    fclose(fp);
    print_heap(arr, end);

    printf("Enter key:"); scanf("%d", &try_count);
    for(int a = 0; a < try_count; a++)
    {
      heap_deletion(arr, &end);
    }

    free(arr);
    return 0;
}
