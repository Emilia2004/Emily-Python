#include <stdio.h>
int main(){
	int number = 0;
	int digit = 0;
	scanf("%i",&number);
	if(number>12){
		while(number != 0){
		digit = number%10;
		printf("%i",digit);
		number = number / 10;
		}
	}
	else{
		printf("Number is invalid");
	}
}
