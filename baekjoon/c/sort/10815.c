#include <stdio.h>
#include <stdlib.h>

int cmp(const int* a, const int* b) {
    return *(int*)a > *(int*)b;
}

int binaryCmp(int arr[], int n, int s){
    int mid, left = 0, right = n-1;
    while (right >= left) {
        mid = (left +right)/2;
        if (s == arr[mid])
            return 1;
        if (s < arr[mid])
            right = mid -1;
        else
            left = mid + 1;
    }

    return 0;
}

int main(){
    int n, m, s;
    scanf("%d", &n);
    int* arr = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    qsort(arr, n, sizeof(int), cmp);
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &s);
        printf("%d\n", binaryCmp(arr, n, s));
    }
    free(arr);
    return 0;
    }
