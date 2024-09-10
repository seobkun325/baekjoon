#include <stdio.h>
#include <string.h>
#define SIZE 10000

typedef struct Stack{
  int data[SIZE];
  int top;
}Stack;

void initStack(Stack* s) {
  s->top = -1;
}

int isEmpty(Stack* s){
  if(s->top == -1) return 1;
  else return 0;
}

int isFull(Stack* s){
  if(s->top == SIZE-1) return 1;
  else return 0;
}

void push(Stack* s, int n){
  if (!isFull(s)){
    s->top++;
    s->data[s->top] = n;
  }
}

int top(Stack* s){
  if (!isEmpty(s)){
    return s->data[s->top];
  }
  else return -1;
}

int size(Stack* s){
  return s->top+1;
}

int pop(Stack* s){
  if(!isEmpty(s)){
    int n = s->data[s->top];
    s->top--;
    return n;
  }
  else return -1;
}

int main(){
  int t;
  Stack s;
  initStack(&s);
  scanf("%d", &t);
  while(t--){
    char control[6];
    scanf("%s", control);
    if (strcmp(control, "push") == 0){
      int x;
      scanf("%d", &x);
      push(&s, x);
    }
    else if (strcmp(control, "pop") == 0){
      printf("%d\n",pop(&s));
    }
    else if (strcmp(control, "size") == 0){
      printf("%d\n",size(&s));
    }
    else if(strcmp(control, "empty") == 0){
      printf("%d\n",isEmpty(&s));
    }
    else if(strcmp(control, "top") == 0){
      printf("%d\n",top(&s));
    }
  }
  return 0;
}