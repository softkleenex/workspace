    #include<stdio.h>

    int main(){
    int data = 0; scanf("%d", &data);
    char current;
    scanf("\n %c", &current);
    int current_index = current - 'A';
    printf("%d", current_index);
    
    return 0;
    }
