Frequency distribution
=======================
Assumptions:
- the programming language is Python, i.e. "simple code" is likely to be
  expensive and we are unlikely to get all the way to O(N), and
- the frequency table will stay reasonably small.

Two implementations to return unique elements in falling order of frequency:
- frequency_naive: straight-forward dict-based version, roughly O(nlogn) + O(n)
- frequency_charonly: optimized for 9-bit char sequences and should in theory
  be close to O(n); alas, the cost of ord() is such that it tends to lose to 
  naive implementation.

In order to run tests and profiling, please run `make-random-gorp.sh` first to
create a large pile of random characters.

Profiling run:
```
$ uname -a
Linux wonky 4.1.0-2-amd64 #1 SMP Debian 4.1.5-1 (2015-08-15) x86_64 GNU/Linux
$ cat /proc/cpuinfo
...
model name      : Intel(R) Core(TM) i7 CPU         920  @ 2.67GHz
cpu cores       : 4
...
```
Given a file of 14 million random characters (see ./make-random-gorp.sh), 
and a random sample of 14 million words from a corpus of 200 words, typical 
run times. As can be seen, nearly all time is spent at python level:
```
$ python -V
Python 2.7.6
$ python ./profile_freqdist.py

frequency_naive on chars
         622 function calls in 1.701 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.701    1.701 <string>:1(<module>)
        1    1.701    1.701    1.701    1.701 freqdist.py:2(frequency_naive)
      308    0.000    0.000    0.000    0.000 freqdist.py:9(<lambda>)
      308    0.000    0.000    0.000    0.000 {cmp}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'iteritems' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {sorted}


frequency_naive on words
         2344 function calls in 2.448 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.448    2.448 <string>:1(<module>)
        1    2.447    2.447    2.448    2.448 freqdist.py:2(frequency_naive)
     1169    0.000    0.000    0.001    0.000 freqdist.py:9(<lambda>)
     1169    0.000    0.000    0.000    0.000 {cmp}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'iteritems' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
        1    0.000    0.000    0.001    0.001 {sorted}
```
Given that most time is spent executing high-level statements, pypy comes in 
handy:
```
$ pypy -V
Python 2.7.10 (b0a649e90b66, Apr 28 2016, 08:57:01)
[PyPy 5.1.1 with GCC 4.8.2]

$ pypy ./profile_freqdist.py

frequency_naive on chars
         629 function calls in 0.546 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.546    0.546 <string>:1(<module>)
        1    0.545    0.545    0.546    0.546 freqdist.py:1(frequency_naive)
      312    0.000    0.000    0.000    0.000 freqdist.py:8(<lambda>)
      312    0.000    0.000    0.000    0.000 {cmp}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'iteritems' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}


frequency_naive on words
         2337 function calls in 1.102 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.102    1.102 <string>:1(<module>)
        1    1.100    1.100    1.102    1.102 freqdist.py:1(frequency_naive)
     1166    0.001    0.000    0.002    0.000 freqdist.py:8(<lambda>)
     1166    0.001    0.000    0.001    0.000 {cmp}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'iteritems' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
```
