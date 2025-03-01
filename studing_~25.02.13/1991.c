#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//https://www.acmicpc.net/problem/1991
//11:14~
//~01:10
//20:10~
//20~30


typedef struct tree{
    struct tree* left;
    struct tree* right;
    char spell;
}tree;

void init_tree(tree* temp)
{
    temp->left = NULL;
    temp->right = NULL;
    temp->spell = '.';
}


void preorder(tree *current)
{
    printf("%c", current -> spell);
    if(current -> left != NULL)
        preorder(current->left);
    if(current -> right != NULL)
        preorder(current->right);
    return ;
}

void inorder(tree *current)
{
    if(current -> left != NULL)
        inorder(current->left);
    printf("%c", current -> spell);
    if(current -> right != NULL)
        inorder(current->right);
    return ;
}


void postorder(tree *current)
{
    if(current -> left != NULL)
        postorder(current->left);
    if(current -> right != NULL)
        postorder(current->right);
    printf("%c", current -> spell);
    return ;
}




int main(){
int len = 0;
scanf("%d ", &len);

tree** tree_list = (tree**)malloc(sizeof(tree*)*len);//tree포인터 배열

for(int a = 0; a < len; a++)
{
    tree_list[a] = (tree*)malloc(sizeof(tree));
    init_tree(tree_list[a]);
    tree_list[a] -> spell = 'A'+((int)a);//차례대로 A(A+0), B(A+1)....
}

for(int a = 0; a < len; a++)
{
    char current;
    scanf(" %c", &current);
    int current_index = current - 'A';//A, B, C를 0, 1, 2..로 변환, tree_list[index]로 사용
    char left, right = '.';
    scanf(" %c %c", &left, &right);
    int left_index = left - 'A'; 
    int right_index = right-'A';

    if(left != '.')
    {
        tree_list[current_index]->left = tree_list[left_index];
    }
    else
    {
     tree_list[current_index]->left = NULL;   
    }

       if(right != '.')
    {
        tree_list[current_index]->right = tree_list[right_index];
    }
    else
    {
     tree_list[current_index]->right = NULL;   
    }
    
}

preorder(tree_list[0]);
printf("\n");
inorder(tree_list[0]);
printf("\n");
postorder(tree_list[0]);



return 0;
}