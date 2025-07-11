#include<stdio.h>

int main()
{

       int a;
       int i;
       printf("Enter any number: ");
       scanf("%d",&a);
       int f=1;
        if(a==0)
       {
                printf("Factorial not possible: ");
       }
       else if(a==1)
       {
       printf("Factorial is 1.");
       }
        else
        {
                for(i=a;i>=1;i--)
                {
                        f=f*i;
                                
                                
                 }
        printf("%d",f);
        }
        return 0;
}
       
