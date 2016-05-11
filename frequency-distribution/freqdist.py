# Given an iterator of elements, returns its unique elements 
def frequency_naive(data):
    table = {}
    for lmnt in data:
        try:
            table[lmnt] += 1
        except KeyError:
            table[lmnt] = 1
    reply = sorted(table.iteritems(), lambda x,y: cmp(x[1], y[1]))
    reply.reverse()
    return [x for (x,y) in reply]

# Special, optimized version that assumes we operate on 8-bit characters,
# as per exercise example. Depressingly, this beats the naive version only 
# with pypy GIL optimizations because of the large number of GIL traversals
# incurred by ord().
def frequency_charonly(data):
    table = [0] * 256
    for lmnt in data:
        table[ord(lmnt)] += 1

    reply = sorted(zip(table, [chr(n) for n in xrange(256)]))
    reply.reverse()
    return [y for (x,y) in reply if x > 0]

frequency = frequency_naive