#ifndef WALLET_H
#define WALLET_H

#include <Arduino.h>
#include "EEPROM.h"

char write_wallet_private();
char write_wallet_public();
char verify_wallet(String source);
char share_pub();
void read_wallet(int *source, int *dest);

#endif
