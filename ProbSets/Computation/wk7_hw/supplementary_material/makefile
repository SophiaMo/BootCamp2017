### CPP compiler wrapper
CXX=mpicxx

### Optimization flags
FFLAGS=-O3

#######################################################################

all: broadcast.cpp.exec allreduce.cpp.exec scatter.cpp.exec pi.cpp.exec

#######################################################################

## Exercise 1
broadcast.cpp.exec: broadcast.cpp
	$(CXX) $(FFLAGS) broadcast.cpp -o broadcast.cpp.exec

## Exercise 2
allreduce.cpp.exec: allreduce.cpp
	$(CXX) $(FFLAGS) allreduce.cpp -o allreduce.cpp.exec

## Exercise 3
scatter.cpp.exec: scatter.cpp
		$(CXX) $(FFLAGS) scatter.cpp -o scatter.cpp.exec

## Exercise 4
pi.cpp.exec: pi.cpp
		$(CXX) $(FFLAGS)  pi.cpp -o pi.cpp.exec

#######################################################################

clean :
	rm -f *.exec

