#include <stdio.h>

int n;
int seq[100];

void generate(int idx, int len)
{
    if (idx == len)
    {
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < n; i++)
            sum1 += seq[i];
        for (int i = n; i < len; i++)
            sum2 += seq[i];

        if (sum1 == sum2)
        {
            for (int i = 0; i < len; i++)
                printf("%d", seq[i]);
            printf(" ");
        }
        return;
    }

    seq[idx] = 0;
    generate(idx + 1, len);
    seq[idx] = 1;
    generate(idx + 1, len);
}

int main()
{
    printf("Enter N : ");
    scanf("%d", &n);
    generate(0, 2 * n);
    printf("\n");
    return 0;
}
