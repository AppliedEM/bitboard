//#include "BigNumber.h"
#include "BigNumber.h"
#include "point.h"
#include "ecdsa.h"
#include "wallet.h"
#include "jerk.h"
#include <Adafruit_NeoPixel.h>

//s120|107303582290733097924842193972465022053148211775194373671539518313500194639752|31263864094075372764364165952345735120266142355350224183303394048209903603471|
//private: 43913397594144996512580295960367186541366168895507672003765477422550381072204
//pubx:    53237820045986896539096637357322002537362350769420441605069248472301971758546
//puby:    49407176618187043960559197373734381057571970898731550795341045595301080938882
//const char* s = "115792089237316195423570985008687907852837564279074904382605163141518161494337";
//BigNumber N = BigNumber(s);
const char signbyte = 's';
const char walletbyte = 'w';
const char setpublicbyte = 'l';
const char verifywalletbyte = 'v';
const char publicbyte = 'p';
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(1, D7, NEO_GRB + NEO_KHZ800);


String wallet_priv = String("43913397594144996512580295960367186541366168895507672003765477422550381072204");
String wallet_pubx = String("53237820045986896539096637357322002537362350769420441605069248472301971758546");
String wallet_puby = String("49407176618187043960559197373734381057571970898731550795341045595301080938882");

int  wallet_priv_addr = 100;
int  wallet_pubx_addr = 300;
int  wallet_puby_addr = 500;

const int timeout = 20;
const bn privatekey = "1337";
char delim = '|';

const int buttonpin = D6;
const int securitytimeout = 3000;

//char wallet[200] = {0};

void setcolor(char r, char g, char b)
{
	pixels.setPixelColor(0, pixels.Color(r,g,b));
	pixels.show();
}

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


uint32_t jerk = 0;
static int taskCore = 0;

void initvalues()
{
  wallet_priv = String(read_wallet(wallet_priv_addr));
  wallet_pubx = String(read_wallet(wallet_pubx_addr));
  wallet_puby = String(read_wallet(wallet_puby_addr));
}

void setup()
{
  BigNumber::begin();
  Serial.begin(115200);
  EEPROM.begin(wallet_puby_addr+200);
  pinMode(buttonpin, INPUT);
  pixels.begin();
  initvalues();
  Serial.println("privkey:");
  Serial.println(wallet_priv);
  Serial.println("pubkeyx:");
  Serial.println(wallet_pubx);
  Serial.println("pubkeyy:");
  Serial.println(wallet_puby);

  init_imu();

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
  point sig = ecdsa::sign(bn(z.c_str()), bn(r.c_str()), bn(k_inv.c_str()), bn(wallet_priv.c_str()));
  setcolor(150,0,0);
  bool issafe = false;
  for(int x = 0; x< securitytimeout; x++)
  {
	  if(digitalRead(buttonpin)==0)
	  {
		  issafe = true;
	  }
	  delay(1);
  }
  
  if(issafe == true)
  {
	  setcolor(0,0,150);
	Serial.println(sig.x.toString());
	Serial.println(sig.y.toString());
  }
  else
  {
	Serial.println(String(-1));
	Serial.println(String(-1));
  }
}

void writetomemory(String val, int addr)
{
  for(int x = 0; x< val.length(); x++)
  {
    EEPROM.write(addr+x, val[x]);
  }
  EEPROM.write(addr+val.length(), delim);
  EEPROM.commit();
}

void handleprivatekey()
{
  String priv = readuntil(delim);
  writetomemory(priv, wallet_priv_addr);
}

void handlepublickey()
{
  String x = readuntil(delim);
  String y = readuntil(delim);
  writetomemory(x, wallet_pubx_addr);
  writetomemory(y, wallet_puby_addr);
}

double ledintense = 0;
char max = 150;
bool goingup = true;
double inc = .025;
void runled()
{
	if(goingup)
	{
		if(ledintense >= max)
		{
			goingup = false;
		}
		ledintense += inc;
	}
	else
	{
		if(ledintense <= 1)
		{
			goingup = true;
		}
		ledintense -= inc;
	}
	setcolor(0,0,(char)ledintense);
}

void loop()
{
	runled();
  if(Serial.available())
  {
    char b = Serial.read();
    if(b == signbyte)
    {
      handlesign();
    }
    else if (b == walletbyte)
    {
      handleprivatekey();
      initvalues();
    }
    else if (b == verifywalletbyte)
    {
      verify_wallet(wallet_priv);
	  Serial.println();
      verify_wallet(wallet_pubx);
	  Serial.println();
      verify_wallet(wallet_puby);
	  Serial.println();
    }
    else if(b == publicbyte)
    {
      share_pub();
    }
    else if(b == setpublicbyte)
    {
      handlepublickey();
      initvalues();
    }
  }
}
