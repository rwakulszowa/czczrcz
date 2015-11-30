CXX=clang
CFLAGS=-g

all: functions.o czczrcz.o main

functions.o: functions.h functions.c
	$(CXX) functions.c -o functions.o $(CFLAGS) -c

czczrcz.o: czczrcz.h czczrcz.c
	$(CXX) czczrcz.c -o czczrcz.o $(CFLAGS) -c

main: main.c czczrcz.o functions.o
	$(CXX) main.c czczrcz.o functions.o -o main

clean:
	rm main *.o
