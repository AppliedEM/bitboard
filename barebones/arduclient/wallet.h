#ifndef WALLET_H
#define WALLET_H

#include <Arduino.h>
#include "EEPROM.h"

char write_wallet_private();
char write_wallet_public();
char verify_wallet(String source);
String read_wallet(int begin);
char share_pub();
#endif
