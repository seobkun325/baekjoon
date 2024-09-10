#include <stdio.h>

int main(){
  int b = 3;
  int* a;
  a = &b;
  printf("%d\n", *a);
}