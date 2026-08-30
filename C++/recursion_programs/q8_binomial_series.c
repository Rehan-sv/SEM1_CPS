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

long ncr(int n, int r)
{
    return fact(n) / (fact(r) * fact(n - r));
}

float calculate(float x, int n, int term)
{
    if (term > n)
        return 0;
    float sign = (term % 2 == 0) ? 1 : -1;
    float value = sign * ncr(n, term) * power(x, term);
    return value + calculate(x, n, term + 1);
}

int main()
{
    float x;
    int n;
    printf("Input the value of x : ");
    scanf("%f", &x);
    printf("Input the value of n : ");
    scanf("%d", &n);

    printf("The value of (1-%.2f)^%d is : %f\n", x, n, calculate(x, n, 0));
    return 0;
}
