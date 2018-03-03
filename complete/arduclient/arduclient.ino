//#include "BigNumber.h"
#include "BigNumber.h"
#include "point.h"
#include "ecdsa.h"

//s120|107303582290733097924842193972465022053148211775194373671539518313500194639752|31263864094075372764364165952345735120266142355350224183303394048209903603471|
//const char* s = "115792089237316195423570985008687907852837564279074904382605163141518161494337";
//BigNumber N = BigNumber(s);
const char signbyte = 's';
const int timeout = 20;
const bn privatekey = "43913397594144996512580295960367186541366168895507672003765477422550381072204";
const char delim = '|';

void printBignum (BigNumber & n)
{
  char * s = n.toString ();
  Serial.println (s);
  free (s);
}  // end of printBignum

void debug1()
{
  Serial.println("beginning program");

  bn z(120);
  bn k(100);

  bn r("107303582290733097924842193972465022053148211775194373671539518313500194639752");
  bn k_inv("31263864094075372764364165952345735120266142355350224183303394048209903603471");
  bn secret(1337);
  Serial.println("beginning sign...");
  //Serial.println((x1*y1).toString());
  Serial.println("SIGNED HASH:");
  point p3 = ecdsa::sign(z, r, k_inv, secret);
  Serial.println(p3.tostring());
  Serial.println("finished sign.");
}

void setup()
{
  BigNumber::begin();
  Serial.begin(115200);

}

void waitforbuffer(const int timeout)
{
  for(int x = 0; x< timeout; x++)
  {
    if(Serial.available())
      break;
    delay(1);
  }
}

String readuntil(char delim)
{
  delay(timeout);
  String output = "";
  char b = Serial.read();
  if(b == delim)
    return output;
  while(b != delim && Serial.available())
  {
    waitforbuffer(timeout);
    output = output + b;
    b = Serial.read();
  }
  return output;
}

bn handlesign()
{
  String z = readuntil(delim);
  String r = readuntil(delim);
  String k_inv = readuntil(delim);
  point sig = ecdsa::sign(bn(z.c_str()), bn(r.c_str()), bn(k_inv.c_str()), privatekey);
  Serial.println(sig.x.toString()+String(delim));
  Serial.println(sig.y.toString()+String(delim));
}

void loop()
{
  if(Serial.available())
  {
    char b = Serial.read();
    if(b == signbyte)
    {
      handlesign();
    }
  }
}
