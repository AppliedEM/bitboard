#include "wallet.h"


extern int  wallet_priv_addr;
extern int  wallet_pubx_addr;
extern int  wallet_puby_addr;
extern String wallet_priv;
extern String wallet_pubx;
extern String wallet_puby;
extern const char delim;

char write_wallet_private(){ //Read wallet into memory and copy to eeprom
  delay(20);
	int i = 0;
  while(!Serial.available());
  char b = Serial.read();
	if (b != '|'){
    while(Serial.available()){
		  wallet_priv[i] = Serial.read();
		  EEPROM.write(wallet_priv_addr, wallet_priv[i]);
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

char write_wallet_public(){
  delay(20);
	int i = 0;
  while(!Serial.available());
  char b = Serial.read();
	if (b == '|'){
    while(Serial.available()){
		  //Get x part of pub key
		  wallet_pubx[i] = Serial.read();
		  EEPROM.write(wallet_pubx_addr, wallet_pubx[i]);
		  if (wallet_pubx[i] == '|'){
				  i = 0;
				  break;
		  }
		  i++;
		  if (i > 200){ //if wallet is too long
		  	return -1;
    	}
		  //Get y part of pub key
		  wallet_puby[i] = Serial.read();
		  if (wallet_puby[i] == '|')
			  break;
		  EEPROM.write(wallet_puby_addr, wallet_puby[i]);
		  if (wallet_puby[i] == '|')
			  break;
		  i++;
		  if (i > 200){ //wallet is too long
			  return -1;
		  }
		  else{
			  return 1;
		  }
    }
	}
}

char verify_wallet(String source){
	//FIXME: Should hash rather than leak wallet
  for(int i = 0; i<200; i++){
    if (source[i] != '|')
      Serial.print(source[i]);
  }
  Serial.println("|");
	return 0;
}

char share_pub(){
  for(int i = 0; i<400; i++){
      Serial.println(wallet_pubx);
      Serial.println(wallet_puby);
	  return 1;
  }
}

String read_wallet(int begin)
{
  char b = (char)EEPROM.read(begin);
  String outp = "" + String(b);
  for(int i = begin+1; i<begin+200 && b != delim; i++)
  {
    b = EEPROM.read(i);
    if(b != delim)
      outp = outp + String(b);
  }
  return outp;
}
