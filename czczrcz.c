#include "czczrcz.h"
#include <stdio.h>
#include <string.h>

void
avgConvergence(const czczrcz* data,
               const unsigned int dataLen,
               const unsigned char bitsCount,
               float* result)
{
  int i, j;
  int scores[bitsCount];

  memset(scores, 0, bitsCount * sizeof(int));

  // Iterate over all elements and count set bits
  for (i = 0; i < dataLen; ++i) {
    unsigned char el = data[i].convergence;

    for (j = 0; j < bitsCount; ++j) {
      unsigned char mask = 1 << j;

      if (el & mask) {
        scores[j] += 1;
      }
    }
  }

  // Compute the average convergence
  for (i = 0; i < bitsCount; ++i) {
    result[i] = (float)scores[i] / dataLen;
  }

  return;
}

czczrcz
createCzczrcz(const unsigned int input,
              const unsigned char bits,
              bool(*fn)(const unsigned char))
{
  bool res = fn(input);
  unsigned char conv = res ? input : ~input;
  czczrcz ans;
  ans.input = input;
  ans.bits = bits;
  ans.output = res;
  ans.convergence = conv;

  return ans;
}

void
printCzczrcz(czczrcz* in)
{
  printf("Bits: %02x Input: %02x Output: %d Convergence: %02x\n",
         in->bits, in->input, in->output, in->convergence);
}

void
printConvergence(const float* conv,
                 const unsigned char bits)
{
  unsigned int i;

  for (i = 0; i < bits; i++) {
      printf("Bit %d: %f\n", i, conv[i]);
  }
}

bool
fnXor(const unsigned char input)
{
  unsigned char a = (input & 2) >> 1;
  unsigned char b = input & 1;

  return a ^ b;
}

bool
fnOr(unsigned char input)
{
  unsigned char a = (input & 2) >> 1;
  unsigned char b = input & 1;

  return a | b;
}
