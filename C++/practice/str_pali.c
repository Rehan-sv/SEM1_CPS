#include <stdio.h>

int main()
{
    int n;
    char str[100];
    int i;

    printf("Enter the size: ");
    scanf("%d", &n);

    printf("Enter the string: ");
    scanf("%s", str);

    for(i = n - 1; i >= 0; i--)
    {
        if(str[i] != str[n - 1 - i])
        {
            printf("not pali");
            return 0;
        }
    }

    printf("pali");

    return 0;
}