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


void merge(Person* list, Person* extra, int left, int mid, int right) {
    int i = left;     
    int j = mid + 1;  
    int k = left;     

    while (i <= mid && j <= right) {
        if (list[i].key <= list[j].key) { // key는 정렬 기준 값
            extra[k++] = list[i++];
        } else {
            extra[k++] = list[j++];
        }
    }

    while (i <= mid) { // 왼쪽 배열에서 남은 값 복사
        extra[k++] = list[i++];
    }
    while (j <= right) { // 오른쪽 배열에서 남은 값 복사
        extra[k++] = list[j++];
    }
}


void mergePass(Person* list, Person* extra, int n, int s) {
    int i = 0;
    while (i <= n - 2 * s) {//i ~ i+2*s 가 n을 넘지 않게
        merge(list, extra, i, i + s - 1, i + 2 * s - 1); // 두개의 s크기 배열 머지
        i += 2 * s;
    }
    if (i + s < n) { //남근거 처리
        merge(list, extra, i, i + s - 1, n - 1);
    } else {
        for (int j = i; j < n; j++) {
            extra[j] = list[j];
        }
    }
}


void mergeSort(Person* list, int n){
    Person*extra = (Person*)malloc(sizeof(Person) * n);
    int s = 1;
    while (s < n)
    {
        mergePass(list, extra, n ,s);
        s *= 2;
        mergePass(extra, list, n ,s);
        s *= 2;
        
    }
    printf("[Recursive merge sort]\n");
    printlist(list, n);
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