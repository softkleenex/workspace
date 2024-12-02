//20211111470 이상재
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define left(a) (a*2 +1)
#define right(a) (a*2 + 2) 

void swap(char* temp1, char* temp2)
{
    char temp[100];
    strcpy(temp, temp1);
    strcpy(temp1, temp2);
    strcpy(temp2, temp);
}

void heapify(char* arr[], int here, int size) {//위에서 아래로 내려가면, max heap 만족하는지 확인
    int left = here * 2 + 1;
    int right = here * 2 + 2;
    int max = here;
    if (left < size && strcmp(arr[left], arr[max]) > 0)
        max = left;
    if (right < size&& strcmp(arr[right], arr[max]) > 0)
        max = right;
    
    if (max != here) {
        swap(arr[here], arr[max]);
        heapify(arr, max, size);
    }
}

void buildHeap(char* arr[], int size) {
    int i,j;
    for (i = size / 2 - 1; i >= 0; i--) {//가장 마지막 노드의 부모노드 ~ 루트 노드 까지 heapify
        heapify(arr, i, size);
    }
}

void heapSort(const char* arr[],int size) { 
    char** arr2 = (char**)malloc(sizeof(char*) * size);
    for(int i = 0; i < size; i++)
        {
            arr2[i] = (char*)malloc(sizeof(char*));
            strcpy(arr2[i], arr[i]);
        }

    int treeSize;
    buildHeap(arr2, size);//max heap 완성
    for (treeSize = size - 1; treeSize >= 0; treeSize--) {
        swap(arr2[0], arr2[treeSize]);
        buildHeap(arr2, treeSize);
    }

    printf("[After heap sort]\n");
    for(int i = 0; i < size; i++)
        {  
            printf("%s ", arr2[i]);
            free(arr2[i]);
        }
    free(arr2);
}



	int main(){
		
		const char* arr[] = {"Simba", "Mufasa", "Nala", "Timon", "Pumbaa", "Scar", "Zazu", "Rafiki", "Shenzi", "Banzai", "Ed"};
		int n =   sizeof(arr)/ sizeof(arr[0]);
        heapSort(arr, n);

	
		return 0;
		}