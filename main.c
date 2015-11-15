#include "czczrcz.h"
#include <stdio.h>

int main() {
  const int range = 4;
  const int input_count = 1 << range;

  int i;

  // Array of binary inputs, outputs and stuff
  czczrcz data[input_count];

  for (i = 0; i < input_count; ++i) {
    data[i] = createCzczrcz(i, range, fnOr);
  }

  float avc[range];
  avgConvergence(data, input_count, range, avc);
  printConvergence(avc, range);

  return 0;
}
