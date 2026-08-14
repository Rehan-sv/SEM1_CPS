#include <stdio.h>

int main(){
    char name[50];
    int marks[5];
    int sum=0;
    int avg;
    int max;
    
    printf("Enter the students ");
    Scanf("%s",name);

    for(int i=0;i<5;i++){
        print("Enter the marks ",i+1);
        scanf("%d",marks[i]);

        sum=sum+marks[i];
        avg=sum/5;

        max=marks[i];
        if(marks[i]>max){
            max=marks[i];
        }

    }
    printf("\nStudent %s scored a total of %d, averaging %.2f. Their highest mark was %d.\n", name, sum, avg, max);
}
