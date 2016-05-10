import time
from freqdist import frequency_naive, frequency_charonly

def test_basic_operation():
    assert frequency_naive([]) == []
    assert frequency_naive([6,1,3,3,6,3]) == [3,6,1]
    assert frequency_naive(['a','b','b','c','b','a']) == ['b','a','c']
    assert frequency_naive(['that', 'this', 'this']) == ['this', 'that']
    assert frequency_naive('assamass') == ['s', 'a', 'm']

def test_frequency_charonly():
    assert frequency_charonly([]) == []
    assert frequency_charonly(['a','b','b','c','b','a']) == ['b','a','c']

def test_compare_results():
    base = open('./random-gorp').read()
    res1 = frequency_naive(base)
    res2 = frequency_charonly(base)
    assert res1 == res2
