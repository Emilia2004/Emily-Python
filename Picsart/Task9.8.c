#include <stdio.h>
int main(){
	int size = 5;
	int arr[size];
	int k = 0;
	for(int i=0;i<size;++i){
		scanf("%i",&k);
		arr[i] = k;
		}
	int max = arr[0];
	for(int i=1;i<size;++i){
		if(arr[i]>max){
			max = arr[i];
		}
	}
	printf("The maximum element is: ");
	printf("%i",max);

}
