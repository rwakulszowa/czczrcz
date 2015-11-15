#include <stdbool.h>

typedef struct czczrcz
{
    unsigned char input;
    bool output;
    unsigned char convergence;
    unsigned char bits;
} czczrcz;

czczrcz
createCzczrcz(const unsigned int input,
              const unsigned char bits,
              bool(*fn)(const unsigned char));

void
printCzczrcz(czczrcz* in);

void
avgConvergence(const czczrcz* data,
               const unsigned int dataLen,
               const unsigned char bitsCount,
               float* result);

void
printConvergence(const float* conv,
                 const unsigned char bits);

bool
fnXor(unsigned char input);

bool
fnOr(unsigned char input);
