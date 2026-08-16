#include <stdio.h>

int main()
{
    char a[100] = "HeL#284!Lo23Coder";

    int n, sum = 0;

    scanf("%d", &n);

    for(int i = 0; i < n; i++)
    {
        if(a[i] >= '0' && a[i] <= '9')
        {
            sum += a[i] - '0';
        }
    }

    printf("The sum is %d", sum);

    return 0;
}