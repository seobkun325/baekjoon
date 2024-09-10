#include <stdio.h>

int main(){

  int month[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  char *date[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
  int n, m;
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n-1; i++){
    m +=month[i];
  }
  printf("%s", date[m%7]);
}