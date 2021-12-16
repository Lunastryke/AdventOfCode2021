#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

int main(void) {
    std::string text;
    std::ifstream data_file("day7_input.txt");
    std::vector<int> pos;
    while(std::getline(data_file, text, ',')) {
        pos.push_back(stoi(text));
    }
    std::cout << "Size: " << pos.size() << '\n';
    std::vector<int>::iterator result;
    result = std::max_element(pos.begin(),pos.end());
    std::cout << "Max: " << pos[std::distance(pos.begin(),result)] << '\n';
    std::vector<int> final_pos(pos[std::distance(pos.begin(),result)], 0);
    for (int i = 0; i < final_pos.size(); i++) {
        for (int j = 0; j < pos.size(); j++) {
            // Part 1
            // final_pos[i] += std::abs(pos[j]-i);
            // Part 2
            int sum = 0;
            for (int k = std::abs(pos[j]-i); k > 0; k--) {
                sum += k;
            }
            final_pos[i] += sum;
        }
    }
    result = std::min_element(final_pos.begin(),final_pos.end());
    std::cout << "Closest: " << std::distance(final_pos.begin(), result) << '\n';
    std::cout << "Fuel Spent : " << final_pos[std::distance(final_pos.begin(), result)] << '\n';
    // for (int i = 0; i < final_pos.size(); i++) {
    //     std::cout << i << " : " << final_pos[i] << '\n';
    // }
}