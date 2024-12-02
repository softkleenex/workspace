//2021111470 이상재
#include <stdio.h>
#include <stdlib.h>
#define fname "D:\\my_note2_openthis\\school\\24.11.27\\in.txt"
//#define fname "in.txt"

typedef struct Person
{
    char name[20];
    int key;
}Person;


void printlist(Person* list, int n)
{
    for(int i = 0; i < n; i++)
    {
        printf("%s: %d\n", list[i].name, list[i].key);
    }
}


void merge(Person* list, Person* temp, int left, int mid, int right) {
    int i = left;    
    int j = mid + 1; 
    int k = left;   

    // 두 부분 배열을 병합
    while (i <= mid && j <= right) {
        if (list[i].key < list[j].key) {
            temp[k++] = list[i++];
        } else {
            temp[k++] = list[j++];
        }
    }

    // 왼쪽 부분 배열의 나머지 복사
    while (i <= mid) {
        temp[k++] = list[i++];
    }

    // 오른쪽 부분 배열의 나머지 복사
    while (j <= right) {
        temp[k++] = list[j++];
    }

    // 임시 배열을 원래 배열로 복사
    for (i = left; i <= right; i++) {
        list[i] = temp[i];
    }
}


void mergeSort(Person* list, int n) {
    Person* temp = (Person*)malloc(sizeof(Person) * n);
    printf("Merge sort 진행중\n");

  
    for (int s = 1; s < n; s *= 2) {
        for (int left = 0; left < n; left += 2 * s) {
            int mid = left + s - 1;
            int right = (left + 2 * s - 1 < n) ? (left + 2 * s - 1) : (n - 1);
            
            if(mid < right)
            {
            merge(list, temp, left, mid, right);
            }
        }
            printf("\ns: %d\n", s);
            printlist(list, n);
    }
    printf("\n[Merge sort 완료]\n");
    printlist(list, n);

    free(temp);
}



int main(){
    FILE *fp1 = fopen(fname, "r"); if(fp1 == NULL) {printf("file error"); return -1;}
    int count = 0; fscanf(fp1, "%d", &count);
    Person* list = (Person*)malloc(sizeof(Person) * count);
    for(int i = 0; i < count; i++)
    {
        fscanf(fp1, "%s", list[i].name);
        fscanf(fp1, "%d", &list[i].key);
    }
 
    mergeSort(list, count);
    

    free(list);
    fclose(fp1);
    return 0;
}