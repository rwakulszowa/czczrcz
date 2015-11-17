#include <stdbool.h>
#include <stdlib.h>

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
              bool(*fn)(const unsigned int));

void
printCzczrcz(czczrcz* in);

typedef struct czArray
{
    unsigned long int len;
    bool(*fn)(const unsigned int);
    czczrcz* cz;
} czArray;

int
createCzArray(czArray* res,
              const unsigned int* inputs,
              const unsigned long inputsLen,
              const unsigned char inputBits,
              bool(*fn)(const unsigned int));


void
avgConvergence(const czczrcz* data,
               const unsigned int dataLen,
               const unsigned char bitsCount,
               float* result);

void
printConvergence(const float* conv,
                 const unsigned char bits);

bool
fnXor(unsigned int input);

bool
fnOr(unsigned int input);
