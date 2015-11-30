#include "czczrcz.h"
#include "functions.h"
#include <stdio.h>

int main() {
  const int range = 4;
  const int input_count = 1 << range;

  unsigned int i;
  czArray czdata;
  unsigned int inputs[input_count];

  // Prepare inputs
  for (i = 0; i < input_count; ++i) {
    inputs[i] = i;
  }

  if (
    createCzArray(&czdata, inputs, input_count, range, fnOr) < 0
     ) { return -1; }

  float avc[range];
  avgConvergence(czdata.cz, input_count, range, avc);
  printConvergence(avc, range);

  return 0;
}
