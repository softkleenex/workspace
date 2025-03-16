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
}data;

data* read_file(){
    FILE* fp1 = fopen(file_name, "r");
    fscanf(fp1, "%d",  &count);
    data* data1 = (data*)malloc(count * sizeof(data));
    for(int i = 0; i < count; i++)
    {
        fscanf(fp1, " %s", data1[i].name);
        fscanf(fp1, " %d", &data1[i].score);
    }

    

    fclose(fp1);
    return data1;
}



void quick_sort(data* data_arr, int start, int end)
{  
    if(start >= end)  {return ;}
    

    printf("pivot: %d(%s)\n", data_arr[start].score, data_arr[start].name);
    data pivot = data_arr[start]; 

    int low = start+1; int high = end;

    while(low <= high)
        {//조건에 맞는 한, 계속해서 swap
             while (low <= end && data_arr[low].score < pivot.score) {
                low++;
            }
            while (high > start && data_arr[high].score >= pivot.score) {
                high--;
            }
            if(low < high)
            {
                data temp = data_arr[low];
                data_arr[low] = data_arr[high];
                data_arr[high] = temp;
            }
        }

    //피벗을 가운데로 옮긴다
    data temp = data_arr[high];
    data_arr[high] = data_arr[start];
    data_arr[start] = temp;

    quick_sort(data_arr, start, high -1);//left
    quick_sort(data_arr, high + 1, end);//right
}



int main(){
    data* readed_data = read_file();
    printf("[after quick sort]\n");
    quick_sort(readed_data, 0, count-1);
    printf("\n\n");

    for(int i = 0; i < count; i++)
    {
        printf("%s : %d\n", readed_data[i].name, readed_data[i].score);
    }

      

    free(readed_data);  
    return 0;
}