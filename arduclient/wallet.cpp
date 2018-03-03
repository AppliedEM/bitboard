#include "wallet.h"


int wallet_addr = 0;
char wallet[200];

char write_wallet(){
  delay(20);
	int i = 0;
  while(!Serial.available());
  char b = Serial.read();
	if (b == '|'){
    while(Serial.available()){
		  wallet[i] = Serial.read();
		  EEPROM.write(wallet_addr, wallet[i]);
		  i++;
    }
		if (i > 200){ //wallet is too long
				return -1;  
		}
		else{
				return 1;
       
		}
	}	
}

char verify_wallet(){
	//FIXME: Should hash rather than leak wallet
  for(int i = 0; i<200; i++){
    //if (wallet[i] != '|')
      Serial.print(wallet[i]);
  }
  Serial.println();
	return 0;
}

char read_wallet(){
    for(int i = wallet_addr; i<200; i++){
        wallet[i] = EEPROM.read(i);
    }
} //TODO
