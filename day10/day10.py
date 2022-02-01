from binascii import Incomplete
from collections import deque

def main(data):
    brace_match = {'{':'}','[':']','(':')','<':'>'}
    brace_score = {'}':1197,']':57,')':3,'>':25137}
    brace_completion_score = {'(':1,'[':2,'{':3,'<':4}
    # Enter code here
    brace_errors = []
    auto_complete_points = []
    for row in data:
        brace_stack = deque()
        incomplete_flag = True
        auto_completion_points = 0
        for brace in row:
            if brace in brace_match:
                brace_stack.append(brace)
            else:
                curr_brace = brace_match[brace_stack.pop()]
                if curr_brace != brace:
                    brace_errors.append(brace)
                    incomplete_flag = False
                    break
        if incomplete_flag:
            while brace_stack:
                auto_completion_points *= 5
                auto_completion_points += brace_completion_score[brace_stack.pop()]
            auto_complete_points.append(auto_completion_points)

    err_cost = 0
    for i in brace_errors:
        err_cost += brace_score[i]
    print('Incorrect Cost: ', err_cost)
    print(auto_complete_points)
    print('Auto Complete points: ', sorted(auto_complete_points)[len(auto_complete_points)//2])

    
if __name__ == "__main__":
    with open("day10_input.txt", 'r') as file:
        data = file.read().splitlines()
    main(data)
