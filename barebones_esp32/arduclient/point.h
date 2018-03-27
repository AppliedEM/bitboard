#define bn BigNumber

class point
{
  public:
    bn x;
    bn y;
    bn a;
    bn b;
    //point(bn, bn, bn, bn);
    point(const bn&,const bn&, const bn&,const bn&);
    point(const point&);
    ~point();
    point operator+(const point&);
    String tostring();
};

point operator*(int, point);
point operator*(const bn&, const point&);
