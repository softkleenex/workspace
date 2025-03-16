#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//2021111470


//left가 null이면, left를 이전에 방문한 노드의 포인터로 
//right가 null, 이후에 방문할 포인터로
typedef struct tree{
    char spell;
    struct tree* left;
    struct tree* right;
    int l_b;
    int r_b;
}tree;

void init(tree* temp, char spell)
{
    temp->spell = spell;
    temp->left = NULL;
    temp->right = NULL;
    temp->l_b = 0;
    temp-> r_b = 0;
}


tree* insucc(tree*temp)//inorder successor>inorder에서의 다음, 현재노드의 다음 목적지를 제시함
{
//r이 t라면, r로 이동,
//r이 f라면, r로 이동후에 l이 true인 node까지 l을 이용하여 이동한다.
//예제로 확인, H D I B E A F C G
    tree* current = temp->right;
   if(!(temp->r_b))//r이 f라면
    {
        while(!(current->l_b))//left가 참일떄까지 left로 이동한다
            current = current->left; 
        //left가 참에 도달하면 종료
        return current;
    }
    //r이 t라면

    return current;    
}


void tinorder(tree* root)
{
    tree* successor = root;
    while(1)
    {
        successor = insucc(successor);
        if(successor == root)//목적지가 더미노드라면
            break;
        printf("%2c", successor->spell);
    }
  //  printf("end");
}




int main(){
    tree root; init(&root, '-'); 
    tree A; init(&A, 'A');
    tree B; init(&B, 'B'); 
    tree C; init(&C, 'C');
    tree D; init(&D, 'D');
    tree E; init(&E, 'E');
    tree F; init(&F, 'F');
    tree G; init(&G, 'G');
    tree H; init(&H, 'H');
    tree I; init(&I, 'I');
    root.left = &A; root.right = &root;
    A.left = &B; A.right = &C;
    B.left = &D; B.right = &E;
    C.left = &F; C.right = &G;
    D.left = &H; D.right = &I;
    E.left = &B; E.right = &A; E.l_b = 1; E.r_b = 1;
    F.left = &A; F.right = &C; F.l_b = 1; F.r_b = 1;
    G.left = &C; G.right = &root; G.l_b = 1; G.r_b = 1;
    H.left= &root; H.right = &D; H.l_b = 1; H.r_b = 1;
    I.left= &D; I.right = &B; I.l_b = 1; I.r_b = 1;

    tinorder(&root);


    return 0;
}