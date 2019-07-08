#include<stdio.h> 
#include<stdlib.h>

int main() 
{ 
    const int PORT_LED = 26;  
    const int FREQUENCY = 100; 
    const float SLEEP_TIME = 1.0f/FREQUENCY;  
    const char MESSAGE[8] = "qwertyui"; 
      
	printf("############################################## \n");
	printf("CONFIGURATION:");
	printf("PORT_LED: %d \n", PORT_LED );
	printf("FREQUENCY: %d \n", FREQUENCY );
	printf("SLEEP_TIME: %f \n", SLEEP_TIME );
	printf("MESSAGE: %s \n", MESSAGE);
	printf("############################################## \n");
    
	
    return 0; 
} 