#include <stdio.h>

int main()
{
    int n, original, digit, rev = 0;

    printf("Enter a number: ");
    scanf("%d", &n);

    original = n;

    while(n > 0)
    {
        digit = n % 10;
        rev = rev * 10 + digit;
        n = n / 10;
    }

    if(rev == original)
    {
        printf("Palindrome");
    }
    else
    {
        printf("Not Palindrome");
    }

    return 0;
}