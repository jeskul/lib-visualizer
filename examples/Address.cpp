#include "Address.h"
#include <iostream>

Address::Address(const std::string& city, const std::string& street)
    : city(city), street(street) {}

void Address::display() const {
    std::cout << street << ", " << city << "\n";
}
