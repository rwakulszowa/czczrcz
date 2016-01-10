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

def split_bool(elements, test, cutoff):
    # A kind of a stub to simulate the splitting functionality for bools
    # TODO: make the condition look always the same: Trait.condition(el) within(bounds)
    tops, lows = [], []

    for e in elements:
        value = test(e)

        if value < cutoff:
            lows.append(e)
        else:
            tops.append(e)

    return (lows, tops)
