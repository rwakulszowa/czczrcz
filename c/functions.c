#include "functions.h"

bool
fnXor(const unsigned int input)
{
  unsigned int a = (input & 2) >> 1;
  unsigned int b = input & 1;

  return a ^ b;
}

bool
fnOr(unsigned int input)
{
  unsigned int a = (input & 2) >> 1;
  unsigned int b = input & 1;

  return a | b;
}
