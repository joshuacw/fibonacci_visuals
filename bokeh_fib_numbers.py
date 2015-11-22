import scipy.constants
import argparse
from bokeh.plotting import figure, output_file, show
from bokeh.charts import Histogram, output_file, show
from fib_math.functions import nth_term, fib_list, prime_list, phi_compare

phi = scipy.constants.golden

parser = argparse.ArgumentParser(description= \
        "A visual display of the Fibonacci sequence.")
parser.add_argument("integer", type = int, help = \
        "Type in the number of Fibonacci terms to be shown.")
parser.add_argument('--debug', '--d', action = 'store_true')
args = parser.parse_args()

#data for graphs
#x = range(args.integer + 1)
#y = fib_list(args.integer)
#y1 = prime_list(args.integer)

x1 = range(2, args.integer + 1)
y2 = map(phi_compare, range(2, args.integer + 1)) 

#output to static HTML file
#output_file("lines.html", title="Growth of Fibonacci Sequence")
output_file("histogram.html")

# creating Fibonacci growth plot and phi plot with title and axis labels
#p = figure(title="Growth of Fibonacci Sequence vs. Prime numbers", \
        #x_axis_label='Term number', y_axis_label='Value')
p = Histogram(x1, y2, title="Convergence of Approx. to True Value of Phi") 

#add a line renderer with legend and line thickness
#p.line(x, y, legend="Fibonacci terms", line_width=2, line_color="red")
#p.line(x, y1, legend="Prime number terms", \
        #line_width=3, line_color="blue", line_dash="4 4")

#show results
show(p)

print ""
print "The number {0} term in the Fibonacci sequence is {1}."\
        .format(int(args.integer), y[args.integer])
print ""
print "The first terms of the Fibonacci sequence out to term {} are:"\
        .format(int(args.integer))
print fib_list(args.integer)
print ""
print "The first terms of prime numbers out to term {} are:"\
        .format(int(args.integer))
print prime_list(args.integer)
print ""
print "The value of the quotient of the last two terms in the sequence is: {}"\
        .format(float(y[args.integer]) / float(y[args.integer - 1]))
print "The true value of phi is: {}".format(phi)
print ""
print "The quotient of the last two terms of the sequence match the true value of phi out to {} digits."\
        .format(phi_compare(args.integer))
