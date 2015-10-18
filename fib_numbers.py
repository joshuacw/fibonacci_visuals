import scipy.constants, argparse

phi = scipy.constants.golden
fib_list = [0, 1]

parser = argparse.ArgumentParser(description="A visual display of the Fibonacci sequence.")
parser.add_argument("integer", type = int, help = "Type in the number of Fibonacci terms to be shown.")
args = parser.parse_args()

#implementing Binet's formula to produce the Nth term
def nth_term(term):
    return int(round((phi**term - (1 - phi)**term) / 5**0.5))

print "The number {0} term in the Fibonacci sequence is {1}.".format(int(args.integer), nth_term(args.integer))

def fib_terms(term): #a list producing the first N terms
    for i in range(2, term + 1): 
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list 
print ""
print "The first terms of the Fibonacci sequence out to term {} are:".format(int(args.integer))
print fib_terms(args.integer)
print ""
print "The value of the quotient of the last two values in the sequence is: {}".format(float(fib_list[args.integer]) / float(fib_list[args.integer - 1]))
print "The true value of phi is: {}".format(phi) 
