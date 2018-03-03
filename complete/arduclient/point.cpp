#include "BigNumber.h"
#include <math.h>
#include "point.h"
#include "ecdsa.h"
//#include <string>
#include <stdio.h>
//#include <iostream>

using namespace std;

/*point G(
  bn("55066263022277343669578718895168534326250603453777594175500187360389116729240"),
  bn("32670510020758816978083085130507043184471273380659243275938904335757337482424"),
  bn(0),
  bn(0)
);

bn N = "115792089237316195423570985008687907852837564279074904382605163141518161494337";

*/

//const point ecdsa::G(bn(120), bn(50), bn(0), bn(0));

const bn N = "115792089237316195423570985008687907852837564279074904382605163141518161494337";

point::point(const bn& xi,const bn& yi, const bn& ai,const bn& bi)
{
  x = xi;
  y = yi;
  a = ai;
  b = bi;
}

point::point(const point& p)
{
  x = p.x;
  y = p.y;
  a = p.a;
  b = p.b;
}

point::~point()
{
  ~x;
  ~y;
  ~a;
  ~b;
}

point point::operator+(const point& other)
{
  //Serial.println("b1");

  /*if((a != other.a) || (b != other.b))
  {
    Serial.print("b-1");
    return point(-1,-1,a,b);
  }*/
  //Serial.println("b2");

  if(x == other.x and y != other.y)
    return point(-1,-1,a, b);
  //Serial.println("b3");
  if (x != other.x)
  {
    bn s = (other.y - y) / (other.x - x);
    bn x2 = (s*s) - x - other.x;
    bn y2 = s*(x-x2) - y;
    return point(x2, y2, a, b);
  }
  else
  {
    //bn s = ((bn(3)*(x*x)) + a) / (bn(2)*y);
    bn s1 = x*x;
    //Serial.println("b5");
    bn s2 = bn(3);
    //Serial.println("b6");
    bn s3 = bn(2);
    //Serial.println("b7");
    bn s4 = s2*s1;
    //Serial.println("b8");
    bn num = s4+a;
    //Serial.println("b9");
    bn den = s3*y;
    //Serial.println("b10");
    bn s = num/den;
    //Serial.println("b11");


    //bn s((bn(3)*(x*x)) / (bn(2)*y));
    //Serial.println("b5");
    bn x2 = (s*s) - bn(2*x);
    //Serial.println("b6");
    bn y2 = (s*(x-x2)) - y;
    //Serial.println("b7");
    point p(x2, y2, a, b);
    return p;
  }
}

String point::tostring()
{
  String outp = "x: " + String(x.toString()) + "\ny: " + String(y.toString()) + "\na: " + String(a.toString()) + "\nb: " + String(b.toString());
  //String outp = "x: " + String(x) + "\ny: " + String(y) + "\na: " + String(a) + "\nb: " + String(b);
  return outp;
}

point operator*(int coeff, point p)
{
  point p2(p.x, p.y, p.a, p.b);
  point p3(p.x, p.y, p.a, p.b);
  for(int x =0; x< coeff-1; x++)
  {
    p2 = p2+p3;
  }
  return p2;
}

point operator*(const bn& coeff, const point& p)
{

  point p2(p.x, p.y, p.a, p.b);
  bn decr(1);
  for(int x =0; x< coeff-decr; x++)
  {
    p2 = p2+p;
  }
  return p2;
}

bn pow2(bn a, bn power, bn modulo)
{
  bn out = a;
  bn dec = 2;

  for(bn x = 0; x < power-dec; x++)
  {
    //Serial.println(String("a: ") + a.toString());
    //Serial.println(String("modulo: ") + modulo.toString());
    out = bn((out*a)%modulo);

    //Serial.println(out);
  }
  return out;
}

point ecdsa::sign(bn z,bn r,bn k_inv, bn secret)
{
  /*Serial.println(String("N: ") + N.toString());
  Serial.println(String("z: ") + z.toString());
  Serial.println(String("r: ") + r.toString());
  Serial.println(String("k_inv: ") + k_inv.toString());
  Serial.println(String("secret: ") + secret.toString());*/

  bn s = ((z + (r*secret)) * k_inv) % N;
  return point(r,s, 0,0);
}
