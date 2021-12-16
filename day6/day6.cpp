#include <iostream>
#include <vector>
#include <fstream>

#include "lanternfish.cpp"

int main(void) {
    std::string text;
    std::ifstream data_file("day6_input.txt");
    std::vector<LanternFish *> fishTank;
    std::vector<int> fishBuckets(9, 0);
    while(std::getline(data_file, text, ',')) {
        fishTank.push_back(new LanternFish(std::stoi(text)));
        fishBuckets[stoi(text)] += 1;
    }

    // Time passes...
    int days = 80;
    for (int i = 0; i < days; i++) {
        for (int j = 0; j < fishTank.size(); j++) {
            LanternFish* lanternFish_ptr = fishTank[j]->tick();
            if (lanternFish_ptr != NULL) {
                fishTank.push_back(lanternFish_ptr);
            }
        }
    }
    std::cout << "Day " << days << ' ' << fishTank.size() << '\n';

    // Part 2
    int daycount = 0;
    FishBuffer fishBuffer = FishBuffer();
    for (int i = 0; i < 7; i++) {
        fishBuffer.push(fishBuckets[i]);
    }
    while (daycount != 256) {
        daycount++;
        fishBuffer.nextDay();
    }
    std::cout << "Day 256: " << fishBuffer.count() << '\n';
}