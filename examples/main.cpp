#include "Person.h"
#include "Address.h"
#include "Company.h"
#include <iostream>

int main() {
    Address home("New York", "5th Avenue");
    Company work("OpenAI");

    Person john("John Doe");
    john.setAddress(&home);
    john.setCompany(&work);

    john.displayInfo();

    return 0;
}
