#include <stdio.h>

void decToBinary(int n)
{
    if (n > 1)
    {
        decToBinary(n / 2);
    }
    printf("%d", n % 2);
}

int main()
{
    int n;
    printf("Input any decimal number : ");
    scanf("%d", &n);
    printf("The Binary value of decimal no. %d is : ", n);
    decToBinary(n);
    printf("\n");
    return 0;
}
