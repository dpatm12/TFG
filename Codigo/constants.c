#include <stdio.h>
#include "constants.h"

void showConstants(){
    printf("############################################## \n");
	printf("CONFIGURATION:");
	printf("PORT_LED_RX: %d \n", PORT_LED_RX );
	printf("PORT_LED_TX: %d \n", PORT_LED_TX );
	printf("FREQUENCY: %d \n", FREQUENCY );
	printf("SLEEP_TIME: %f \n", SLEEP_TIME );
	printf("MESSAGE: %s \n", MESSAGE);
	printf("############################################## \n");
}
