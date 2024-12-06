#ifndef PERSON_H
#define PERSON_H

#include <string>
#include "Address.h"
#include "Company.h"

class Person {
private:
    std::string name;
    Address* address; // Person has an Address
    Company* company; // Person works at a Company
public:
    Person(const std::string& name, Address* address = nullptr, Company* company = nullptr);
    void setAddress(Address* address);
    void setCompany(Company* company);
    void displayInfo() const;
};

#endif // PERSON_H
