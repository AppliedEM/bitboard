#include "point.h"
#include <iostream>

using namespace std;

bn secret = 145;

void debug1()
{
  bn x1 = 1;
  bn y1 = 1;
  bn a1 = 1;
  bn b1 = 1;

  bn x2 = 2;
  bn y2 = 2;
  bn a2 = 1;
  bn b2 = 1;

  point a(x1, y1, a1, b1);
  point b(x2, y2, a2, b2);

  cout << "a: " << a.tostring() << endl;
  cout << "b: " << b.tostring() << endl;
  cout << (a+b).tostring() << endl;
  cout << (5*a).tostring() << endl;
}

int main()
{
  debug1();
}
