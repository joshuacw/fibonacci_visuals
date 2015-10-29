import scipy.constants
import argparse
import decimal
from bokeh.plotting import figure, output_file, show
decimal.getcontext().prec = 1000

phi = scipy.constants.golden

parser = argparse.ArgumentParser(description="A visual display of the Fibonacci sequence.")
parser.add_argument("integer", type = int, help = "Type in the number of Fibonacci terms to be shown.")
args = parser.parse_args()

#implementing Binet's formula to produce the Nth term
def nth_term(term):
    return int(round((phi**term - (1 - phi)**term) / 5**0.5))

#produces a list of the first N Fibonacci terms
def fib_list(term): 
    fib_list = [0, 1]
    for i in range(2, term + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list

#produces a list of the first N prime numbers
def prime_list(term): 
    prime_list = [2]
    number = 3

    while len(prime_list) < term + 1:
        counter = 0
        for n in range(2, number):
            if number % n == 0:
                counter += 1
            else:
                counter += 0
        if counter == 0:
            prime_list.append(number)
        number += 1
    return prime_list

# check how many digits quotient of last 2 terms matches phi out to
def phi_match(term):
    phi1000list = []
    phi_dec_list = []
    with open('phi1000.txt', 'r') as phi:
        phi1000 = phi.read()
        phi_dec = str(decimal.Decimal(nth_term(term)) / decimal.Decimal(nth_term(term - 1)))

        for char in phi1000:
            phi1000list.append(char)

        for char in phi_dec: 
            phi_dec_list.append(char)

    for i in range(1001):
        if(phi1000list[i] == phi_dec_list[i]):
            i += 1
        else:
            break

    return i - 1

#data for graph
x = range(args.integer + 1)
y = fib_list(args.integer)
y1 = prime_list(args.integer)

#output to static HTML file
output_file("lines.html", title="Growth of Fibonacci Sequence")

# creating a new plot with title and axis labels
p = figure(title="Growth of Fibonacci Sequence vs. Prime numbers", x_axis_label='Term number', y_axis_label='Value')

#add a line renderer with legend and line thickness
p.line(x, y, legend="Fibonacci terms", line_width=2, line_color="red")
p.line(x, y1, legend="Prime number terms", line_width=3, line_color="blue", line_dash="4 4")

#show results
show(p)

print ""
print "The number {0} term in the Fibonacci sequence is {1}.".format(int(args.integer), nth_term(args.integer))
print ""
print "The first terms of the Fibonacci sequence out to term {} are:".format(int(args.integer))
print fib_list(args.integer)
print "The first terms of prime numbers out to term {} are:".format(int(args.integer))
print prime_list(args.integer)
print ""
print "The value of the quotient of the last two terms in the sequence is: {}".format(float(y[args.integer]) / float(y[args.integer - 1]))
print "The true value of phi is: {}".format(phi)
print ""
print "The quotient of the last two terms of the sequence match the true value of phi out to {} digits.".format(phi_match(args.integer))
