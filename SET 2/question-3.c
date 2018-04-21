#include <stdio.h>

int main() {
  int array[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  for (int i = 0; i < 10; i++) 
  {
    printf("%d \n", array[i] * array[i]);
  }
  return 0;
}
