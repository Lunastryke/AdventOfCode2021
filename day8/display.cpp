#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <map>

class Display {
    std::vector<int> displayed_num;
    std::vector<std::string> input;
    std::map<char, std::vector<char>> mapping;
    std::map<int , std::vector<char>> reference;
    std::map<int , std::vector<int>> num_reference;
    std::map<char, std::vector<int>> num_mapping;

    public:
    Display() {
        reference[0] = {'a','b','c','e','f','g'};
        reference[1] = {'c','f'};
        reference[2] = {'a','c','d','e','g'};
        reference[3] = {'a','c','d','f','g'};
        reference[4] = {'b','c','d','f'};
        reference[5] = {'a','b','d','f','g'};
        reference[6] = {'a','b','d','e','f','g'};
        reference[7] = {'a','c','f'};
        reference[8] = {'a','b','c','d','e','f','g'};
        reference[9] = {'a','b','c','d','f','g'};
        num_reference[2] = {1};
        num_reference[3] = {7};
        num_reference[4] = {4};
        num_reference[5] = {2,3,5};
        num_reference[6] = {0,6,9};
        num_reference[7] = {8};
    }

    bool input_part1(std::string val) {
        switch (val.length()) {
        case 2:
            return true;
            break;
        case 3:
            return true;
            break;
        case 4:
            return true;
            break;
        case 7: 
            return true;
            break;
        default:
            return false;
            break;
        }
    }

    void input_part2(std::string val) {
        for (int i = 0; i < val.size(); i++) {
            if (num_mapping.find(val[i]) == num_mapping.end()) {
                num_mapping[val[i]] = num_reference[val.size()];
            } else {
                
            }
        }
    }

    void input_part2_old(std::string val) {
        std::vector<char> possible_mappings;
        input.push_back(val);
        switch (val.length())
        {
        case 2:
            possible_mappings = reference[1];
            break;
        case 3:
            possible_mappings = reference[7];
            break;
        case 4:
            possible_mappings = reference[4];
            break;
        case 5:
            possible_mappings = {'a','b','c','d','e','f','g'};
            break;
        case 6:
            possible_mappings = {'a','b','c','d','e','f','g'};
            break;
        case 7: 
            possible_mappings = reference[8];
            break;
        default:
            possible_mappings = {'a','b','c','d','e','f','g'};
            break;
        }
        for (int i = 0; i < val.length(); i++) {
            if (mapping.find(val[i]) == mapping.end()) {
                mapping[val[i]] = possible_mappings;
                std::cout << val[i] << ": Standard mapping : " << mapping[val[i]].size() << '\n';
            } else {
                std::vector<char> new_possible_mappings;
                std::set_intersection(
                    mapping[val[i]].begin(), mapping[val[i]].end(),
                    possible_mappings.begin(), possible_mappings.end(),
                    std::back_inserter(new_possible_mappings));
                mapping[val[i]] = new_possible_mappings;
                std::cout << val[i] << ": ";
                for (auto j = 0; j < new_possible_mappings.size(); j++) {
                    std::cout << new_possible_mappings[j];
                }
                std::cout << '\n';
            }
        }
        return;
    }

    void getResult(std::vector<int> *result) {
        std::cout << mapping['f'].size() << ' ';
        for (int i = 0; i < input.size(); i++) {
            std::vector<char> input_chars(input[i].begin(), input[i].end());
            for (int j = 0; j < 10; j++) {
                if (input_chars == reference[j]) {
                    result->push_back(j);
                    break;
                }
            }
        }
        return;
    }
};