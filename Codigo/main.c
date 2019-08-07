#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <string.h>
#include "constants.h"
#include "main.h"

int main(int argc, char *argv[]){
	char *tx = "tx";
	char *rx = "rx";
    if ( argc != 2){
		printf("ERROR: fallo en el número de argumentos \n");
		return 1;
	}
	showConstants();
	if ( strcmp(argv[1],tx) == 0){
		printf("Estoy en tx");
		mainTx();
		return 0;
	}
	if ( strcmp(argv[1],rx) == 0){
		printf("Estoy en rx");
		return 0;
	}
    return 1;
}

int mainTx(){
	pthread_t thread1, thread2;
	int ret1, ret2;
	
	ret1 = pthread_create( &thread1, 
	
	return 0;
	}