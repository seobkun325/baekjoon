#include <stdio.h>

int main(){
  char name[6] = 'Askar';
  unsigned long a;
  sscanf(name, "%1x", &a);
  printf("%lu", a);
}