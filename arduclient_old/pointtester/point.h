#define bn double

class point
{
  public:
    bn x;
    bn y;
    bn a;
    bn b;
    point(bn, bn, bn, bn);
    point(const point&);
    point operator+(const point&);
    char* tostring();
};

point operator*(int, point);
