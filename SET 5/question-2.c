#include <stdio.h>

int main(int argc, char const *argv[]) {
  int ch;
  printf("The program works for the following range of inputs: \n");
  printf("48-57, 65-90, 97-122 \n");
  printf("Enter a number: ");
  scanf("%d", &ch);
  if (ch >= 0 && ch < 128) {
    printf("%c \n", ch);
  }
  return 0;
}
