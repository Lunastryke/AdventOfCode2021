from collections import Counter
from curses import pair_content

def main(data):
    sep = data.index('')
    initial = data[0:sep][0]
    instructions = data[sep+1::]
    p = Polymer(initial, instructions)
    for i in range(40):
        p.next_round()
    print(p.get_ans())
    # Enter code here

class Polymer:
    def __init__(self, initial, instructions):
        self.curr = initial
        self.pair_count = {}
        self.generated_pairs = {}
        self.letter_counts = {}
        self.instr = {}
        for i in instructions:
            inp, oup = i.split(' -> ')
            self.instr[inp] = oup
            self.generated_pairs[inp] = [inp[0] + oup, oup + inp[1]]
        for i in range(len(initial)-1):
            if self.curr[i:i+2] in self.pair_count:
                self.pair_count[self.curr[i:i+2]] += 1
            else:
                self.pair_count[self.curr[i:i+2]] = 1
        for i in self.curr:
            if i not in self.letter_counts:
                self.letter_counts[i] = 1
            else:
                self.letter_counts[i] += 1
        
    
    def next_round(self):
        new_pair_count = {}
        for pair in self.pair_count:
            if self.instr[pair] in self.letter_counts:
                self.letter_counts[self.instr[pair]] += self.pair_count[pair]
            else:
                self.letter_counts[self.instr[pair]] = self.pair_count[pair]
            if self.pair_count[pair] > 0:
                for i in self.generated_pairs[pair]:
                    if i not in new_pair_count:
                        new_pair_count[i] = self.pair_count[pair]
                    else:
                        new_pair_count[i] += self.pair_count[pair]
        self.pair_count = new_pair_count

    def get_curr(self):
        return self.curr

    def get_ans(self):
        print(self.letter_counts)
        return max(self.letter_counts.values()) - min(self.letter_counts.values())

if __name__ == "__main__":
    with open("day14_input.txt", 'r') as file:
        data = file.read().splitlines()
    main(data)
