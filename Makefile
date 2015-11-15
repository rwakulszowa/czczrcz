CXX=clang
CFLAGS=-g

all: czczrcz.o main

czczrcz.o: czczrcz.h czczrcz.c
	$(CXX) czczrcz.c -o czczrcz.o $(CFLAGS) -c

main: main.c czczrcz.o
	$(CXX) main.c czczrcz.o -o main

clean:
	rm main
