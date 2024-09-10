#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
  int n;
  scanf("%d", &n);
  int arr[n];
  for (int i = 0; i < n/2; i++){
    scanf("%d", &arr[i]);
  }
  if (n%2 == 0)
  {
    int arr1[n/2], arr2[n/2];
    for(int i = 0; i < n/2; i++){
      arr1[i] = arr[i];
    }
    for (int i= 0; i < n/2; i++){
      arr2[i] = arr[n/2+i];
    }
  }
  else
  {
  }
  for (int i = 0; i < n/2; i++){
    printf("%d %d", arr1[i], arr2[i]);
  }
  
  return 0;
}