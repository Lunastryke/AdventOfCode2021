#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include "display.cpp"

int main (void) {
    std::string text;
    std::string output_text;
    std::vector<std::string> outputs;
    std::ifstream data_file("day8_input_test.txt");
    Display digit_display = Display();
    int count = 0;
    while(std::getline(data_file, text)) {
        std::string parsed_input = text.substr(0,text.find('|'));
        std::string parsed_output = text.substr(text.find('|')+2);
        std::string buf;
        std::stringstream ss_input(parsed_input);
        std::stringstream ss_output(parsed_output);
        while (ss_input >> buf) {
            digit_display.input_part2(buf);
        } 
        while (ss_output >> buf) {

            // if (digit_display.input_part1(buf)) {
            //     count++;
            // }
            digit_display.input_part2(buf);
        }
    }
    std::cout << count << '\n';
    // std::vector<int> results;
    // digit_display.getResult(&results);
    // std::cout << results[0] << '\n';
}