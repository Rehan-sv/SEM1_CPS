#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *addStrings(const char *num1, const char *num2)
{
    int len1 = strlen(num1);
    int len2 = strlen(num2);
    int maxLen = (len1 > len2 ? len1 : len2) + 1;
    char *result = (char *)malloc(maxLen + 1);
    int i = len1 - 1, j = len2 - 1, k = maxLen - 1;
    int carry = 0;
    result[maxLen] = '\0';

    while (i >= 0 || j >= 0 || carry)
    {
        int d1 = (i >= 0) ? num1[i] - '0' : 0;
        int d2 = (j >= 0) ? num2[j] - '0' : 0;
        int sum = d1 + d2 + carry;
        result[k--] = (sum % 10) + '0';
        carry = sum / 10;
        i--;
        j--;
    }

    char *finalResult = strdup(result + k + 1);
    free(result);
    return finalResult;
}

int check(const char *num, int start, char *num1, char *num2)
{
    int n = strlen(num);
    if (start == n)
        return 1;

    char *sum = addStrings(num1, num2);
    int sumLen = strlen(sum);

    if (start + sumLen > n || strncmp(num + start, sum, sumLen) != 0)
    {
        free(sum);
        return 0;
    }

    int result = check(num, start + sumLen, num2, sum);
    free(sum);
    return result;
}

int isValid(const char *num)
{
    return !(strlen(num) > 1 && num[0] == '0');
}

int isAdditiveSequence(const char *num)
{
    int n = strlen(num);
    for (int i = 1; i <= n - 2; i++)
    {
        for (int j = i + 1; j <= n - 1; j++)
        {
            char num1[100], num2[100];
            strncpy(num1, num, i);
            num1[i] = '\0';
            strncpy(num2, num + i, j - i);
            num2[j - i] = '\0';

            if (!isValid(num1) || !isValid(num2))
                continue;

            if (check(num, j, num1, num2))
                return 1;
        }
    }
    return 0;
}

int main()
{
    char s[100];
    printf("Enter the string to check for additive sequence : ");
    scanf("%s", s);

    if (isAdditiveSequence(s))
        printf("true\n");
    else
        printf("false\n");

    return 0;
}
