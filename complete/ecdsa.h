#include "point.h"

class ecdsa
{
  public:
    static bn sign(bn z,bn k, bn secret) ;
  private:
    point G;
};
