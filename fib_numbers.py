import scipy.constants
import sys

phi = scipy.constants.golden
term = int(sys.argv[1])
fib_list = [0, 1]

#implementing Binet's formula to produce the Nth term
def nth_term(term):
    return int(round((phi**term - (1 - phi)**term) / 5**0.5))

print "The number %d term in the Fibonacci sequence is %d." % (int(sys.argv[1]), nth_term(term))

def fib_terms(term): #a list producing the first N terms
    for i in range(2, term + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list

print ""
print "The first terms of the Fibonacci sequence out to term %d are:" % int(sys.argv[1])
print fib_terms(term)
