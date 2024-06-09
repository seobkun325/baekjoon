#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
  int arr[26];
  memset(arr, 0, sizeof(arr));
  char str[100];
  scanf("%s", str);
  for (int i = 0; str[i] != '\0'; i++){
    arr[(int)(str[i] - 'a')]++;
  }
  for (int i = 0; i < 26; i++){
    printf("%d ", arr[i]);
  }
}