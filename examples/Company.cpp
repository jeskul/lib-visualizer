#include "Company.h"
#include <iostream>

Company::Company(const std::string& name) : name(name) {}

void Company::display() const {
    std::cout << name << "\n";
}
