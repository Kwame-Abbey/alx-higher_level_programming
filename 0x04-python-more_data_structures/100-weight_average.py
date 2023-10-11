#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple
    (<score>, <weight>)
    """
    if my_list:
        total_score = 0
        total_weight = 0
        for tup in my_list:
            total_score += tup[0] * tup[1]
            total_weight += tup[1]

        average = total_score / total_weight
        return average
    else:
        return 0
