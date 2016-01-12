from __future__ import division
from sklearn.cluster import KMeans

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

def split_bool(elements, test, classifier):
    values = [test(e) for e in elements]

    classifier.fit([[v] for v in values])
    means = classifier.cluster_centers_

    groups = {
        0: [],
        1: []
    }

    for el, val in zip(elements, values):
        label = classifier.predict(val)[0]
        groups[label].append(el)

    return [(means[label][0], groups[label], label) for label in groups]

def within(el, bounds, inclusive=False):
    left = bounds[0]
    right = bounds[1]

    if inclusive and el == right:
        return True

    return left <= el < right
