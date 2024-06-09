#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 20

typedef struct Stack{
  char data[SIZE];
  int top;
}Stack;

void init(Stack *s){
  s->top = -1;
}
int isEmpty(Stack *s){
  if(s->top == -1) return 1;
  else return 0;
}
int isFull(Stack *s){
  if(s->top == SIZE-1) return 1;
  else return 0;
}
void push(Stack *s, char c){
  if(!isFull(s)){
    s->top++;
    s->data[s->top] = c;
  }
}
int pop(Stack *s){
  if(!isEmpty(s)){
    s->top--;
    return s->data[s->top+1];
  }
  else return -1;
}
int main(){
  Stack s;
  init(&s);
  int t;
  scanf("%d",&t);
  while(t--){
    char str[1001];
    scanf(" %[^\n]", str);
    for (int i = 0; ; i++){
      if(str[i] == ' ' || str[i] == '\0'){
        while(!isEmpty(&s)){
          printf("%c",pop(&s));
        }
        if (str[i] == ' '){
          printf(" ");
        }
        else if(str[i] == '\0'){
          break;
        }
      }
      else {
        push(&s, str[i]);
      }
    }
    printf("\n");
  }
}