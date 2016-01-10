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

def split_bool(elements, test, cutoff, value_range):
    # A kind of a stub to simulate the splitting functionality for bools
    # TODO: make the condition look always the same: Trait.condition(el) within(bounds)
    lows, tops = [], []
    left_end = value_range[0]
    right_end = value_range[1]

    low_range = (left_end, cutoff)
    high_range = (cutoff, right_end)

    low_condition = lambda x: within(x, low_range)
    high_condition = lambda x: within(x, high_range, inclusive=True)

    for e in elements:
        value = test(e)

        if low_condition(value):
            lows.append(e)
        elif high_condition(value):
            tops.append(e)
        else:
            print ("Warning: element {} matched no conditions".format(e))

    return (
        (lows, low_range, low_condition),
        (tops, high_range, high_condition)
    )

def within(el, bounds, inclusive=False):
    left = bounds[0]
    right = bounds[1]

    if inclusive and el == right:
        return True

    return left <= el < right
