#ifndef ADDRESS_H
#define ADDRESS_H

#include <string>

class Address {
private:
    std::string city;
    std::string street;
public:
    Address(const std::string& city, const std::string& street);
    void display() const;
};

#endif // ADDRESS_H
