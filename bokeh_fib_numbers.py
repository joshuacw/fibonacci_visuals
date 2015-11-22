import scipy.constants
import argparse
from bokeh.io import hplot
from bokeh.plotting import figure, output_file, show
from fib_math.functions import nth_term, fib_list, prime_list, phi_compare

phi = scipy.constants.golden

parser = argparse.ArgumentParser(description= \
        "A visual display of the Fibonacci sequence.")
parser.add_argument("integer", type = int, help = \
        "Type in the number of Fibonacci terms to be shown.")
parser.add_argument('--debug', '--d', action = 'store_true')
args = parser.parse_args()

#data for growth plot 
x_growth = range(args.integer + 1)
y_fib = fib_list(args.integer)
y_prime = prime_list(args.integer)

#data for phi-comparison plot
x_phi = range(2, args.integer + 1)
y_phi = map(phi_compare, range(2, args.integer + 1)) 

#output to static HTML file
output_file("layout.html", title="Fibonacci Fun")

# creating Fibonacci and prime number growth plot 
s1 = figure(plot_width=600, plot_height=600, title="Growth of Fibonacci Sequence vs. Prime numbers", \
        x_axis_label='Term number', y_axis_label='Value')
s1.line(x_growth, y_fib, legend="Fibonacci terms", line_width=2, line_color="red")
s1.line(x_growth, y_prime, legend="Prime number terms", \
        line_width=3, line_color="blue", line_dash="4 4")

#Create phi-comparison plot
s2 = figure(plot_width=600, plot_height=600, title='Phi Estimate vs. Phi', \
        x_axis_label= 'Fibonacci term number', y_axis_label='Matching Digit')
s2.circle(x_phi, y_phi, size=15, color='black', alpha=0.5) 

#Put plots in an HBox
p = hplot(s1, s2)

#show results
show(p)

print ""
print "The number {0} term in the Fibonacci sequence is {1}."\
        .format(int(args.integer), y_fib[args.integer])
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
        .format(float(y_fib[args.integer]) / float(y_fib[args.integer - 1]))
print "The true value of phi is: {}".format(phi)
print ""
print "The quotient of the last two terms of the sequence match the true value of phi out to {} digits."\
        .format(phi_compare(args.integer))
