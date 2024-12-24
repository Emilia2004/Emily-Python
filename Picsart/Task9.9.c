#include <stdio.h>
int main(){
	int size = 5;
	int num = 0;
	int arr[size];
	for(int i=0;i<size;++i){
		scanf("%i",&num);
		arr[i] = num;
	}
	int min = arr[0];
	for(int i=1;i<size;++i){
		if(arr[i]<min){
			min = arr[i];
		}
	}
	printf("The minimum element is: ");
	printf("%i",min);
}
