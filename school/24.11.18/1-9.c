    //2021111470 이상재
    #include <stdio.h>
    #include <string.h>
    #include <stdlib.h>
    #define fn "D:\\my_note2_openthis\\school\\24.11.18\\in.txt"
    //#define fn "in.txt"
    //17:17~ 18:08 19:10~ 20:30 20:50~ 21:17






    int** init_matrix(int v)//2차원 배열 첫 생성
    {
        int** arr = (int**)calloc(v, sizeof(int*));
        for(int i = 0; i < v; i++)
        {
            arr[i] = (int*)calloc(v, sizeof(int));
        }
        return arr;
    }



    void init_edge(FILE *fp1, int v, int **arr)//file 에서 읽어서 배열 구성
    {
        int s = 0; int t = 0; fscanf(fp1, "%d %d", &s, &t);
        arr[s][t] = 1; arr[t][s] = 1;

    }

    int visit(int* visited, int v)//visit 배열 조작 + 출력용
    {
        printf("%d  ",  v);
        visited[v] = 1;
        return v;
    }


    void bfs_component_exe(int **arr, int* visited, int v_len, int v_target)
    {
        int* queue = (int*)calloc(v_len, sizeof(int));
        int front = 0;//반환용
        int rear = 0;//삽입용
        queue[rear] = v_target;//초기노드를 q에 넣고,
        rear++;

        while(front < rear)//q가 빌떄까지
        {
            int cur = queue[front]; front++;
            visit(visited, cur);
            for(int i = 0 ; i < v_len; i++)
                {
                    if(visited[i] == 0 && arr[cur][i] == 1)//큐에서 꺼낸 v의 이웃 v중 미방문 v확인시에 
                        {
                            visited[i] = 1;
                            queue[rear] = i;//queue에 넣는다
                            rear++;
                        }
                }
        }
        free(queue);
    }



    int bfs_component(int **arr, int*visited, int v, int start)//visited 배열을 main에서 받는것으로 변경, main 의 visited 조건에 따라 반복
    {
        bfs_component_exe(arr, visited, v, start);
        printf("\n");
        return start;
    }


    void bfs_exe(int **arr, int* visited, int v_len, int v_target)//1. 큐에서 꺼내 탐색, 2. 해당 큐의 인접 and 미방문 노드 큐에 삽입 3. 큐 빌떄까지 반복
    {
        int* queue = (int*)calloc(v_len, sizeof(int));
        int front = 0;//반환용
        int rear = 0;//삽입용
        queue[rear] = v_target;//초기노드를 q에 넣고,
        rear++;

        while(front < rear)//q가 빌떄까지
        {
            int cur = queue[front]; front++;
            visit(visited, cur);
            for(int i = 0 ; i < v_len; i++)
                {
                    if(visited[i] == 0 && arr[cur][i] == 1)//큐에서 꺼낸 v의 이웃 v중 미방문 v확인시에 
                        {
                            visited[i] = 1;
                            queue[rear] = i;//queue에 넣는다
                            rear++;
                        }
                }
        }
        free(queue);
    }



    int bfs(int **arr, int v)//breath f s
{

    printf("input starting number:");
    int t = 0; scanf("%d",  &t); if(t == -1) {return t;}
    int* visited = (int*)calloc(v, sizeof(int));
    bfs_exe(arr, visited, v, t);
    free(visited);
    printf("\n");
    return t;
}



    void bfs_SpanningTree_exe(int **arr, int* visited, int v_len, int v_target)//bfs에서 visit 만 수정
    {
        int* queue = (int*)calloc(v_len, sizeof(int));
        int front = 0;//반환용
        int rear = 0;//삽입용
        queue[rear] = v_target;//초기노드를 q에 넣고,
        rear++;

        while(front < rear)//q가 빌떄까지
        {
            int cur = queue[front]; front++;
            visited[cur] = 1;
            for(int i = 0 ; i < v_len; i++)
                {
                    if(visited[i] == 0 && arr[cur][i] == 1)//큐에서 꺼낸 v의 이웃 v중 미방문 v확인시에 
                        {
                            printf("(%d, %d)",  cur, i);
                            visited[i] = 1;
                            queue[rear] = i;//queue에 넣는다
                            rear++;
                        }
                }
        }
        free(queue);
    }



    int bfs_SpanningTree(int **arr, int v)//breath f 
{
    printf("input starting number:");
    int t = 0; scanf("%d",  &t); if(t == -1) {return t;}
    int* visited = (int*)calloc(v, sizeof(int));
    bfs_SpanningTree_exe(arr, visited, v, t);
    free(visited);
    printf("\n");
    return t;
}





  void dfs_exe(int **arr, int* visited, int v_len, int v_target)//1. 현재 v 탐색, 현재 v와 인접 + 미방문 노드 탐색
    {
        visit(visited, v_target);
        for(int i = 0; i < v_len; i++)
        {
            if(arr[v_target][i] == 1 && visited[i] == 0)
            {
                dfs_exe(arr, visited, v_len, i);
            }
        }
    }


    int dfs(int **arr, int v)//depth f s
    {
        printf("input starting number:");
        int t = 0; scanf("%d",  &t); if(t == -1) {return t;}
        int* visited = (int*)calloc(v, sizeof(int));
        dfs_exe(arr, visited, v, t);
        free(visited);
        printf("\n");
        return t;
    }


 void dfs_SpanningTree_exe(int **arr, int* visited, int v_len, int v_target)
    {
        visited[v_target] = 1;
        for(int i = 0; i < v_len; i++)
        {
            if(arr[v_target][i] == 1 && visited[i] == 0)
            {
                 printf("(%d,  %d)", v_target, i);
                dfs_SpanningTree_exe(arr, visited, v_len, i);
            }
        }
    }


    int dfs_SpanningTree(int **arr, int v)//depth f s
    {
        printf("input starting number:");
        int t = 0; scanf("%d",  &t); if(t == -1) {return t;}
        int* visited = (int*)calloc(v, sizeof(int));
        dfs_SpanningTree_exe(arr, visited, v, t);
        free(visited);
        printf("\n");
        return t;
    }

  
        int dfs_component(int** arr, int v, int* visited, int start)//depth f s
    {
        dfs_exe(arr, visited, v, start);
        printf("\n");
        return 0;
    }

    void dfs_component_exe(int **arr, int* visited, int v_len, int v_target)
    {
        visit(visited, v_target);
        for(int i = 0; i < v_len; i++)
        {
            if(arr[v_target][i] == 1 && visited[i] == 0)
            {
                dfs_component_exe(arr, visited, v_len, i);
            }
        }
    }

    void free_matrix(int**arr, int v)
    {
        for(int i = 0; i < v; i++)
            {
                free(arr[i]);
            }
        free(arr);
    }


    int main()
    {
        FILE *fp1; fp1 = fopen(fn, "r");
        int v = 0; fscanf(fp1, "%d", &v);
        int** arr = init_matrix(v);
        int edge = 0; fscanf(fp1, "%d", &edge);
        for(int i = 0; i < edge; i++)
        {
            init_edge(fp1, v, arr);
        }

        printf("[DFS]\n");
        while(1)
        {
        if (-1 == dfs(arr, v))
            break;
        }

        printf("[BFS]\n");
        while(1)
        {
        if (-1 == bfs(arr, v))
            break;
        }

        printf("[DFS Component]\n");
        int* visited = (int*)calloc(v, sizeof(int));
        int start = 0;
        for(int i = 0; i < v; i++)
        {
            printf("Component %d:  ", start);
            dfs_component(arr, v, visited, start);
            for(int i2 = 0; i2 < v; i2++)
            {
                if(visited[i2] == 0)
                    {
                        start = i2;
                        break;
                    }
            }
            if(visited[start] == 1) break;
        }
        free(visited);




        printf("[BFS Component]\n");
        int* visited2 = (int*)calloc(v, sizeof(int));
        start = 0;
        for(int i = 0; i < v; i++)
        {
            printf("Component %d:  ", start);
            bfs_component(arr, visited, v, start);
            for(int i2 = 0; i2 < v; i2++)
            {
                if(visited[i2] == 0)
                    {
                        start = i2;
                        break;
                    }
            }
            if(visited[start] == 1) break;
        }

        printf("[DFS Spanning Tree]\n");
        while(1)
        {
        if (-1 == dfs_SpanningTree(arr, v))
            break;
        }

        printf("[BFS Spanning Tree]\n");
        while(1)
        {
        if (-1 == bfs_SpanningTree(arr, v))
            break;
        }


        free(visited);



        free_matrix(arr, v);
        fclose(fp1);
        return 0;
    }
