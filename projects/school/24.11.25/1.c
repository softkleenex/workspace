//2021111470 이상재
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define file_name "D:\\my_note2_openthis\\school\\24.11.25\\in.txt"
//#define file_name "in.txt"


int count = 0; //정렬에 필요

typedef struct data{
    char name[100];
    int score;
    struct data* next;
}data;



data* read_file(){
    FILE* fp1 = fopen(file_name, "r");
    fscanf(fp1, "%d",  &count);
    data* data1 = (data*)malloc(count * sizeof(data));
    for(int i = 0; i < count; i++)
    {
        fscanf(fp1, " %s", data1[i].name);
        fscanf(fp1, " %d", &data1[i].score);
        data1[i].next = NULL;
    }


    fclose(fp1);
    return data1;
}



int main(){
    data* readed_arr = read_file();
    data* insert_sort = NULL;


    for (int i = 0; i < count; i++) // 값 추가
    {
        data* new_data = (data*)malloc(sizeof(data));
        *new_data = readed_arr[i];
        new_data->next = NULL; // 새 노드 초기화

        if (insert_sort == NULL || new_data->score < insert_sort->score) {
            // 리스트가 비었음 or 새로운 데이터가 가장 앞
            new_data->next = insert_sort;
            insert_sort = new_data;
        } else {
            data* temp = insert_sort;
            while (temp->next != NULL && temp->next->score <= new_data->score) {
                temp = temp->next; // 삽입 위치 탐색
            }
            // 노드 삽입
            new_data->next = temp->next;
            temp->next = new_data;
        }
    }
    
    printf("[after insert sort]\n");
    data* temp = insert_sort;
    while(temp != NULL)
        {
            printf("%s : %d\n", temp->name, temp->score);
            temp = temp->next;
        }

    temp = insert_sort;
    while(temp != NULL)
        {
            data* for_free = temp;
            temp = temp->next;
            free(for_free);
        }



    free(readed_arr);    
    return 0;
}