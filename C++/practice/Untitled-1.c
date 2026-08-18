#include<stdio.h>
#include<string.h>
#include<conio.h>
#include <ctype.h>
#include<math.h>
int main()
{
    int dn,r,bn=0,i=0;
    printf("enter the decimal number:");
    scanf("%d",&dn);
    while(dn!=0)
    {
        r=dn%2;
        bn+=r*pow(10,i);
        dn=dn/2;
        i++;
    }
    printf("%d",bn);
}