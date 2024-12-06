# Compiler and flags
CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17
AR = ar
ARFLAGS = rcs

# Source files and object files
SRC = Person.cpp Address.cpp Company.cpp
OBJ = $(SRC:.cpp=.o)

# Static library and main executable
LIB = libproject.a
TARGET = main

# Default rule
all: $(TARGET)

# Building the static library
$(LIB): $(OBJ)
	$(AR) $(ARFLAGS) $@ $^

# Linking the executable with the static library
$(TARGET): main.o $(LIB)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Compiling .cpp files to .o files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Cleaning up
clean:
	rm -f $(OBJ) $(LIB) $(TARGET) *.o

# Phony targets
.PHONY: all clean
