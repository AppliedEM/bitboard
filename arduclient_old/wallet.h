#ifndef WALLET_H
#define WALLET_H

#include <Arduino.h>
#include "EEPROM.h"

char write_wallet_private();
char write_wallet_public();
char verify_wallet(char source[]);
void read_wallet(int *source, int *dest);

#endif
