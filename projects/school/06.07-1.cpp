#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 150

typedef struct {
    int x, y, dist;
} Point;

int maze[MAX][MAX];
int width = 0, height = 0;

bool isValid(int x, int y) {
    return (x >= 0) && (x < height) && (y >= 0) && (y < width) && (maze[x][y] == 1);
}

int bfs() {
    int rowNum[] = { -1, 0, 0, 1 };
    int colNum[] = { 0, -1, 1, 0 };

    bool visited[MAX][MAX] = { false };

    if (maze[0][0] == 0 || maze[height - 1][width - 1] == 0) {
        return -1;
    }

        visited[0][0] = true;
        Point queue[MAX * MAX];
        int front = 0, rear = 0;


        Point start = { 0, 0, 0 };
        queue[rear++] = start;

        while (front != rear) {
            Point curr = queue[front++];
            int x = curr.x;
            int y = curr.y;
            int dist = curr.dist;

            if (x == height - 1 && y == width - 1) {
                return dist;
            }

            for (int i = 0; i < 4; ++i) {
                int row = x + rowNum[i];
                int col = y + colNum[i];

                if (isValid(row, col) && !visited[row][col]) {
                    visited[row][col] = true;
                    Point next = { row, col, dist + 1 };
                    queue[rear++] = next;
                }
            }
        }

        return -1;
    }

    int main()
    {
        FILE* file = fopen("maze.txt", "r");                                                        
        if (file == NULL) {
            perror("Failed to open maze file");
            return EXIT_FAILURE;
        }

        char line[MAX];
        height = 0;
        while (fgets(line, sizeof(line), file)) {
            width = 0;
            for (int j = 0; line[j] != '\n' && line[j] != '\0'; ++j) {
                if (line[j] == '0' || line[j] == '1') {
                    maze[height][width++] = line[j] - '0';
                }
            }
            height++;
        }

        fclose(file);

        printf("Maze dimensions: %d x %d\n", height, width);
        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
                printf("%d", maze[i][j]);
            }
            printf("\n");
        }

        int result = bfs();
        if (result != -1) {
            printf(" shortest path  %d\n", result + 1);
        }
        else {
            printf("No path.\n");
        }

        return 0;
    }


