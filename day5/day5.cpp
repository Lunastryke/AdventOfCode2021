#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

void parser(string, int *, int *, int *, int *);

int main(void) {
    // Reading File
    string text;
    ifstream data_file("day5_input.txt");
    int range = 1000;
    int x1,x2,y1,y2;
    vector<int> grids(range*range,0);
    while(getline(data_file, text)) {
        // String is of format x1,y1 -> x2,y2
        parser(text, &x1, &y1, &x2, &y2);
        // Part 1: 
        if (x1 == x2) {
            if (y1 <= y2) {
                for (int i = y1; i <= y2; i++) {
                    grids[x1 + i*range] += 1;
                }
            } else {
                for (int i = y2; i <= y1; i++) {
                    grids[x1 + i*range] += 1;
                }
            }
        } else if (y1 == y2) {
            if (x1 <= x2) {
                for (int i = x1; i <= x2; i++) {
                    grids[i + y1*range] += 1;
                }
            } else {
                for (int i = x2; i <= x1; i++) {
                    grids[i + y1*range] += 1;
                }
            }
        } else if (abs(y2-y1) == abs(x2-x1)) {
            while (x1 != x2) {
                grids[x1 + y1 * range] += 1;
                if (x1 < x2) {
                    x1++;
                } else if (x1 > x2) {
                    x1--;
                }
                if (y1 < y2) {
                    y1++;
                } else if (y1 > y2) {
                    y1--;
                }
            }
            grids[x1 + y1 * range] += 1;
        }
    //     for (int i = 0; i < grids.size(); i++) {
    //         if (i % range == 0) {
    //             cout << '\n';
    //         }
    //         cout << grids[i] << ' ';
    //     }
    // cout << '\n';
        
    }
    data_file.close();
    int counter = 0;
    // for (int i = 0; i < grids.size(); i++) {
    //     if (i % 10 == 0) {
    //         cout << '\n';
    //     }
    //     cout << grids[i] << ' ';
    // }
    for (int i = 0; i < grids.size(); i++) {
        if (grids[i] > 1) {
            counter++;
        }
    }
    cout << "results: " << counter << '\n';
}

void parser(string text, int *x1, int *y1, int *x2, int*y2) {
    string point1, point2;
    size_t pos = text.find(" -> ");
    point1 = text.substr(0, pos);
    point2 = text.substr(pos+4);
    size_t pos_comma_1 = point1.find(',');
    size_t pos_comma_2 = point2.find(',');
    *x1 = stoi(point1.substr(0, pos_comma_1));
    *x2 = stoi(point2.substr(0, pos_comma_2));
    *y1 = stoi(point1.substr(pos_comma_1+1));
    *y2 = stoi(point2.substr(pos_comma_2+1));
    return;
}