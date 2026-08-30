#include <stdio.h>

int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int main()
{
    int a, b;
    printf("Input 1st number for LCM : ");
    scanf("%d", &a);
    printf("Input 2nd number for LCM : ");
    scanf("%d", &b);

    int lcm = (a * b) / gcd(a, b);
    printf("The LCM of %d and %d :  %d\n", a, b, lcm);
    return 0;
}
