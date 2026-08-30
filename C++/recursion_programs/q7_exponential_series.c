#include <stdio.h>

float power(float x, int n)
{
    if (n == 0)
        return 1;
    return x * power(x, n - 1);
}

long fact(int n)
{
    if (n == 0)
        return 1;
    return n * fact(n - 1);
}

float calculateE(float x, int n, int term)
{
    if (term == n)
        return 0;
    return (power(x, term) / fact(term)) + calculateE(x, n, term + 1);
}

int main()
{
    float x;
    int n;
    printf("Input the value of x : ");
    scanf("%f", &x);
    printf("Input the number of terms : ");
    scanf("%d", &n);

    printf("The value of e^%.2f up to %d terms is : %f\n", x, n, calculateE(x, n, 0));
    return 0;
}
