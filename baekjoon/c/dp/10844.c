#include <stdio.h>

int main(){
  int n;
  scanf("%d", &n);
  int dp[n];
  dp[0]=9;
  for (int i=1; i < n;i++){
    dp[i] = (dp[i-1]*2-i)%100000000;
  }
  printf("%d",dp[n-1]);
}