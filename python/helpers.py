from __future__ import division

def countIf(list, condition):
    """ Count elements in list satisfying the condition """
    return sum(1 if condition(x) else 0 for x in list)

def percentage(list, condition):
    return countIf(list, condition) / len(list)

def separate(elements, condition):
    hits, misses = [], []

    for el in elements:
        if condition(el):
            hits.append(el)
        else:
            misses.append(el)

    return hits, misses

def split_bool(elements, test, value_range):
    # A kind of a stub to simulate the splitting functionality for bools
    tops, lows = [], []

    low = value_range[0]
    top = value_range[1]
    middle = (low + top) / 2

    def low_condition(x):
        return low <= x < middle

    def top_condition(x):
        return middle <= x <= top

    for e in elements:
        value = test(e)

        if low <= value < middle:
            lows.append(e)
        else:
            tops.append(e)

    return (
        (lows, low_condition),
        (tops, top_condition)
    )
