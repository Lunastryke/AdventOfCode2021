0 1 2 3 4 5 6 7 8 9

For a given signal begcd:

if len(signal) in [2,3,4,7]:
    it is obvious which digit it is [1,4,7,8]
else:
    it is [0,2,3,5,6,9]
    if len(signal) == 6 :
        [0, 6, 9]
        if signal contains 1:
            [0, 9]
            if signal contains 4:
                9
            else:
                0
        else:
            6
    if len(signal) == 5:
        [2, 3, 5]
        if signal contains 1:
            3
        else:
            [2, 5]:
            if signal intercept 4 by 3:
                5
            else:
                2