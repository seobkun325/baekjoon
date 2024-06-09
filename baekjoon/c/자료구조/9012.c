#include <stdio.h>

#define size 100
int status = 1;

typedef struct Stack{
  int data[size];
  int top;
}Stack;

void init(Stack *s){
  s->top = -1;
}

int isEmpty(Stack *s){
  return s->top == -1;
}

int isFull(Stack *s){
  return s->top == size - 1;
}

void push(Stack *s){
    s->top++;
}

void pop(Stack *s){
    if(!isEmpty(s)){
      s->top--;
    }
    else
      status = 0;
}


int main(){
  Stack s;
  int t;
  scanf("%d", &t);
  while(t--)
  {
    status = 1;
    init(&s);
    char str[100];
    scanf("%s", str);
    for (int i = 0; str[i] != '\0'; i++)
    {
      if (str[i] == '('){
        push(&s);
      }
      else if (str[i] == ')'){
        pop(&s);
      }
    }
    if (status == 0)
      printf("NO\n");
    else if (!isEmpty(&s))
      printf("NO\n");
    else if (isEmpty(&s))
      printf("YES\n");


  }
}