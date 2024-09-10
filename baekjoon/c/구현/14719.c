#include <stdio.h>
#include <string.h>
#include <stdbool.h>
int main(){
    int h, w;
    scanf("%d %d", &h, &w);
    int map[h][w];
    memset(map, 0, sizeof(map));
    for(int i = 0; i < w; i++){
        int x;
        scanf("%d", &x);
        for(int j = h-1; j >= h-x; j--){
            map[j][i] = 1;
        }
    }
    int sum = 0;
    for (int i = 0; i < h; i++){
        int count = 0;
        bool start = false;
        for (int j = 0; j < w; j++){
            if(map[i][j] == 1){
                if (start == false) start = true;
                else start = false;
            }
            if(start == true & map[i][j] == 0){
                count ++;
            }
        }
        sum += count;
    }
    // for (int i = 0; i < h; i++){
    //     for (int j = 0; j < w; j++) {
    //         printf("%d ", map[i][j]);
    //     }
    //     printf("\n");
    // }
    printf("%d", sum);
    return 0;
}