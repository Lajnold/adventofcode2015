#include <iostream>

const int day20_input = 34000000;

int number_of_presents_part1(int house)
{
    int presents = 0;
    for (int elf = 1; elf <= house; elf++) {
        if (house % elf == 0) {
            presents += elf * 10;
        }
    }
    return presents;
}

int number_of_presents_part2(int house)
{
    int presents = 0;
    for (int elf = 1; elf <= house; elf++) {
        if (house % elf == 0 && house / elf <= 50) {
            presents += elf * 11;
        }
    }
    return presents;
}

void part1()
{
    int house = 0;
    int high = 0;

    while (high < day20_input) {
        int presents = number_of_presents_part1(house);

        if (presents > high) {
            high = presents;
            std::cout << "New high: " << high << " at house: " << house << std::endl;
        }

        if (presents < day20_input) {
            house++;
        }
    }

    std::cout << "House: " << house << std::endl;
}

void part2()
{
    int house = 0;
    int high = 0;

    while (high < day20_input) {
        int presents = number_of_presents_part2(house);

        if (presents > high) {
            high = presents;
            std::cout << "New high: " << high << " at house: " << house << std::endl;
        }

        if (presents < day20_input) {
            house++;
        }
    }

    std::cout << "House: " << house << std::endl;
}

int main()
{
    part1();
    part2();

    return 0;
}
