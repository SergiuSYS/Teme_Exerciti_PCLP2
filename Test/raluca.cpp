#include <iostream>
#include <string>
#include <cctype> // For isdigit

bool containsNumber(const std::string& str) {
    for (char c : str) {
        if (isdigit(c)) {
            return true;
        }
    }
    return false;
}

int main() {
    std::string testStr;
    std::cout << "Enter a string: ";
    std::getline(std::cin, testStr);

    if (containsNumber(testStr)) {
        std::cout << "The string contains a number." << std::endl;
    } else {
        std::cout << "The string does not contain any numbers." << std::endl;
    }

    return 0;
}