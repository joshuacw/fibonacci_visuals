import scipy.constants
import argparse
from bokeh.io import hplot
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool
from class_fib_math.functions import Fib_Math

phi = scipy.constants.golden

parser = argparse.ArgumentParser(description= \
        "A visual display of the Fibonacci sequence.")
parser.add_argument("integer", type = int, help = \
        "Type in the number of Fibonacci terms to be shown. \
        Any integer >= 2 will work.")
parser.add_argument('--debug', '-d', action = 'store_true')
args = parser.parse_args()

if args.debug:
    DEBUG = True

    y_fib = Fib_Math().fib_list(args.integer)
    print ""
    print "The number {0} term in the Fibonacci sequence is {1}."\
        .format(int(args.integer), y_fib[args.integer])
    print ""
    print "The first terms of the Fibonacci sequence out to term {} are:"\
        .format(int(args.integer))
    print Fib_Math().fib_list(args.integer)
    print ""
    print "The first terms of prime numbers out to term {} are:"\
        .format(int(args.integer))
    print Fib_Math().prime_list(args.integer)
    print ""
    print "The value of the quotient of the last two terms in the sequence is: {}"\
        .format(float(y_fib[args.integer]) / float(y_fib[args.integer - 1]))
    print "The true value of phi is: {}".format(phi)
    print ""
    print "The quotient of the last two terms of the sequence match the true value of phi out to {} digits."\
        .format(Fib_Math().phi_compare(args.integer))

else:
    DEBUG = False

    # data for growth plot
    x_growth = range(args.integer + 1)
    y_fib = Fib_Math().fib_list(args.integer)
    y_prime = Fib_Math().prime_list(args.integer)

    # data for phi-comparison plot
    x_phi = range(2, args.integer + 1)
    y_phi = map(Fib_Math().phi_compare, range(2, args.integer + 1))

    # output to static HTML file
    output_file("layout.html", title="Fibonacci Fun")

    # creating Fibonacci and prime number growth plot
    s1 = figure(plot_width=400, plot_height=400, \
            title="Growth of Fibonacci Sequence vs. Prime numbers",\
            title_text_font_size = "12pt",
        x_axis_label='Fibonacci term number', y_axis_label='Value')
    s1.line(x_growth, y_fib, legend="Fibonacci terms", line_width=2, line_color="red")
    s1.line(x_growth, y_prime, legend="Prime number terms", \
        line_width=3, line_color="blue", line_dash="4 4")

    # Create phi-comparison plot
    hover = HoverTool(tooltips = [
        ("F(n) / F(n - 1) matches phi to", "$y digits")
                                ]
                    )
    s2 = figure(plot_width=400, plot_height=400, title='Phi Estimate vs. Phi', \
            title_text_font_size = "12pt",
        x_axis_label= 'Fibonacci term number', y_axis_label='Matching Digits', tools = [hover])
    s2.circle(x_phi, y_phi, size=15, color='black', alpha=0.5)

    # create Fibonacci spiral plot
    # first, get n squares
    b, l, t, r = Fib_Math().get_n_squares(args.integer)

    #then, make sure the ranges of the axes are proper length
    x_low, x_hi, y_low, y_hi = Fib_Math().get_axis_range(args.integer)

    # add in the golden spiral
    x_zero, y_zero, x_one, y_one, cx_zero, cy_zero, cx_one, cy_one = Fib_Math().get_spiral_coord(args.integer)

    # and Bokeh the shit out of it all!
    s3 = figure(width = 400, height = 400, x_range = (x_low, x_hi), y_range = (y_low, y_hi),\
            title="The Golden Spiral", title_text_font_size = "12pt")
    s3.quad(bottom = b, left = l, top = t, right = r, color = 'white', alpha = 1.0, line_color = 'black', line_width = 3)
    s3.bezier(x0 = x_zero, y0 = y_zero, x1 = x_one, y1 = y_one,  cx0 = cx_zero, cy0 = cy_zero, cx1 = cx_one, cy1 = cy_one)

    #Put plots in an HBox ('H' stands for Horizontal)
    p = hplot(s1, s2, s3)

    #show results
    show(p)

    print ""
    print "The number {0} term in the Fibonacci sequence is {1}."\
        .format(int(args.integer), y_fib[args.integer])
    print ""
    print "The first terms of the Fibonacci sequence out to term {} are:"\
        .format(int(args.integer))
    print Fib_Math().fib_list(args.integer)
    print ""
    print "The first terms of prime numbers out to term {} are:"\
        .format(int(args.integer))
    print Fib_Math().prime_list(args.integer)
    print ""
    print "The value of the quotient of the last two terms in the sequence is: {}".format(float(y_fib[args.integer]) / float(y_fib[args.integer - 1]))
    print "The true value of phi is: {}".format(phi)
    print ""
    print "The quotient of the last two terms of the sequence match the true value of phi out to {} digits."\
        .format(Fib_Math().phi_compare(args.integer))
