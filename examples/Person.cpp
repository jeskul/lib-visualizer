#include "Person.h"
#include <iostream>

Person::Person(const std::string& name, Address* address, Company* company)
    : name(name), address(address), company(company) {}

void Person::setAddress(Address* address) {
    this->address = address;
}

void Person::setCompany(Company* company) {
    this->company = company;
}

void Person::displayInfo() const {
    std::cout << "Name: " << name << "\n";
    if (address) {
        std::cout << "Address: ";
        address->display();
    }
    if (company) {
        std::cout << "Company: ";
        company->display();
    }
}
