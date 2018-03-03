//#include <BigNumber.h>
#include "point.h"
#include <math.h>
#include <string>
#include <stdio.h>
#include <iostream>

using namespace std;

point::point(bn xi, bn yi, bn ai, bn bi)
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

point point::operator+(const point& other)
{
  if((a != other.a) || (b != other.b))
    return point(-1,-1,a,b);
  if(x == other.x and y != other.y)
    return point(-1,-1,a, b);
  if (x != other.x)
  {
    bn s = (other.y - y) / (other.x - x);
    bn x2 = pow(s,2) - x - other.x;
    bn y2 = s*(x-x2) - y;
    return point(x2, y2, a, b);
  }
  else
  {
    bn s = ((3*pow(x,2)) + a) / (2*y);
    bn x2 = pow(s,2) - (2*x);
    bn y2 = (s*(x-x2)) - y;
    return point(x2, y2, a, b);
  }
}

char* point::tostring()
{
  string output = "";
  char* outp = new char[50];
  sprintf(outp, "x: %f, y: %f, a: %f, b: %f", x, y, a, b);
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
