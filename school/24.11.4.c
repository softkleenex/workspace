#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAX_QUEUE 500
//2021111470 이상재
//4:28 start

typedef struct node{
    struct node *left;
    struct node *right;
    int data;
}node;





void init_node(node* temp){
    temp-> left = NULL;
    temp -> right = NULL;
    temp-> data = 0;
}




void make_tree(node* temp_root)//현재 노드에서 각 자식의 생성조건을 체크하고, 생성된 자식을 재귀로 체크한다.
{
    //예시를 보니 500이상인 node의 자식x > 500 초과인 node는 미생성인듯?
    
        if(!(500 < 3*(temp_root->data)))
        {
        node* temp_left;
        temp_left = (node*)malloc(sizeof(node)); 
        init_node(temp_left);
        temp_root->left = temp_left;
        temp_left->data = 3*(temp_root->data);

        make_tree(temp_left);
        }
        if(!(500 < temp_root->data*temp_root->data))
        {
        node* temp_right = (node*)malloc(sizeof(node)); 
        init_node(temp_right);
        temp_root->right = temp_right;
        temp_right -> data = (temp_root->data)*(temp_root->data);        
        make_tree(temp_right);
        }
    
}


int height(node* temp_root)
{//왼쪽의 height와 오른쪽 height의 높이중에 큰것을 취하고, +1

     if(temp_root == NULL)
    {
        return 0;
    }


    int left_height = height(temp_root->left);
    int right_height = height(temp_root->right);
    
    int max_height = left_height >= right_height ? left_height : right_height;
    max_height++;


    return max_height;
}


void inorder(node* current){
//왼쪽 방향 탐색 > 실패 시에(if문 통과시에) 현재 노드 출력, 
//현재노드의 오른쪽 탐색 > 유효하면 다시 inorder 시행.
   if(current == NULL) return ;

   if(current -> left != NULL)
    inorder(current->left);

    printf("(%d)  ", current->data);

    if(current -> right != NULL)
        inorder(current->right);
}

//레벨 우선 탐색은 queue 구현 필요

node* queue[MAX_QUEUE];
int front = 0;
int rear = -1;

int queueempty()
{
    return front > rear;
}

int queuefull()
{
    return rear == MAX_QUEUE-1;
}

void enqueue(node *node)
{
    if(!(queuefull()))
        {
            queue[++rear] = node;
        }

}

node* dequeue()
{
    if(!(queueempty()))
        {
            return queue[front++];
        }
    
    return NULL;
}


void Levelorder(node* root)
{//최상 루트 노드 큐에 넣고,
//현재 큐 출력 > 출력한 node의 left, right 유효시에 queue에 넣음... queue가 비워지면 끝



    if(root == NULL) return ;

    enqueue(root);

    while(!queueempty())
    {
        node*current = dequeue();
        printf("(%d)  ", current->data);
        if(current->left != NULL)
        {
            enqueue(current->left);
        }
            if(current->right !=NULL)
        {
            enqueue(current->right);
        }
    }
   
}



int main(){

node* root_start = (node*)malloc(sizeof(node)); 
init_node(root_start);
printf("input number");
scanf("%d", &(root_start->data));
make_tree(root_start);
printf("height: %d\n", height(root_start));
printf("inorder travel:");
inorder(root_start);
printf("\nLevelorder travel:");
Levelorder(root_start);




return 0;
}


