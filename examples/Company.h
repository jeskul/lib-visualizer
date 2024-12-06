#ifndef COMPANY_H
#define COMPANY_H

#include <string>

class Company {
private:
    std::string name;
public:
    Company(const std::string& name);
    void display() const;
};

#endif // COMPANY_H
