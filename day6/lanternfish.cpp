#include <iostream>
#include <vector>
#include <deque>

class LanternFish {
    int timer;
    LanternFish() {
        timer = 9;
    }
    public: 
    LanternFish(int x) {
        timer = x;
    }
    LanternFish* tick() {
        if (timer == 0) {
            timer = 6;
            LanternFish * lanternFish_ptr = new LanternFish();
            return lanternFish_ptr;
        }
        timer--;
        return nullptr;
    }
};

class FishBuffer {
    std::deque<long> oldFish;
    std::deque<long> newFish;
    public:
    FishBuffer() : newFish(2) {}

    void push(int num) {
        oldFish.push_back(num);
    }

    void nextDay() {
        long front_old = oldFish.front();
        long front_new = newFish.front();
        // std::cout << front_new << '\n';
        oldFish.pop_front();
        newFish.pop_front();
        oldFish.push_back(front_new + front_old);
        newFish.push_back(front_old);
    }

    long count() {
        long sum = 0;
        for(int i = 0; i < oldFish.size(); i++) {
            sum += oldFish[i];
        }
        for(int i = 0; i < newFish.size(); i++) {
            sum += newFish[i];
        }
        return sum;
    }
};