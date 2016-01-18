import decimal

class Fib_Math(object):

    def __init__(self):
        pass

    # calculate nth term recursively in n steps
    #may still need to try another algorithm for better accuracy
    def nth_term(self, term):
        a, b = decimal.Decimal(0), decimal.Decimal(1)
        for i in range(term):
            a, b = b, a + b
        return a

    # produces a list of the first N Fibonacci terms
    def fib_list(self, term):
        fib_list = [0, 1]
        for i in range(2, term + 1):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list

    # produces a list of the first N prime numbers
    def prime_list(self, term):
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

    # produces an approx. of phi using the nth and (nth - 1) fib terms
    def phi_approx(self, term):
        thousand_places = decimal.Decimal(10) ** -999
        my_context = decimal.Context(prec = 1000)
        decimal.setcontext(my_context)

        phi_approx = str(decimal.Decimal(Fib_Math().nth_term(term) / Fib_Math().nth_term(term - 1)).quantize(thousand_places))

        return phi_approx

    # compares the approx. of phi with the true value of phi out to 1000 digits
    def phi_compare(self, term):
        approx = Fib_Math().phi_approx(term)
        phi1000list = []
        approx_list = []

        with open('phi1000.txt', 'r') as phi:
            phi1000 = phi.read()

        for char in phi1000:
            phi1000list.append(char)

        for char in approx:
            approx_list.append(char)

        i = 0
        while phi1000list[i] == approx_list[i]:
            i += 1

        if term == 3:
            return 0
        else:
            return i - 1

    # a function to produce n fib squares
    def get_n_squares(self, n):

        b = []
        l = []
        t = []
        r = []

        if n == 1:
            b = [0]
            l = [0]
            t = [1]
            r = [1]

        if n == 2:
            b = [0, 1]
            l = [0, 0]
            t = [1, 2]
            r = [1, 1]

        if n == 3:
            b = [0, 1, 0]
            l = [0, 0, -2]
            t = [1, 2, 2]
            r = [1, 1, 0]

        if n == 4:
            b = [0, 1, 0, -3]
            l = [0, 0, -2, -2]
            t = [1, 2, 2, 0]
            r = [1, 1, 0, 1]

        if n >= 5:
            b = [0, 1, 0, -3]
            l = [0, 0, -2, -2]
            t = [1, 2, 2, 0]
            r = [1, 1, 0, 1]

            fib_terms = [0, 1, 1, 2, 3, 5]
            for i in range(5, n + 1):
                if i % 4 == 1: #for squares going "to the right"
                    b.append(b[i - 2])
                    l.append(r[i - 2])
                    t.append(t[i - 3])
                    r.append(r[i - 2] + fib_terms[i])
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])
                if i % 4 == 2: #for squares going "up"
                    b.append(t[i - 2])
                    l.append(l[i - 3])
                    t.append(t[i - 2] + fib_terms[i])
                    r.append(r[i - 2])
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])
                if i % 4 == 3: #for squares going "to the left"
                    b.append(b[i - 3])
                    l.append(l[i - 2] - fib_terms[i])
                    t.append(t[i - 2])
                    r.append(l[i - 2])
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])
                if i % 4 == 0: #for squares going "down"
                    b.append(b[i - 2] - fib_terms[i])
                    l.append(l[i - 2])
                    t.append(b[i - 2])
                    r.append(r[i - 3])
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])

        return b, l, t, r

    # updating the ranges of the x & y axes for any given number of squares
    def get_axis_range(self, n):
        if n == 0 or n == 1 or n == 2:
            x_low = 0
            x_hi = 2
            y_low = 0
            y_hi = 2
        fib_terms = [0, 1, 1, 2]
        if n >= 3:
            x_low = 0
            x_hi = 2
            y_low = 0
            y_hi = 2
            for i in range(3, n + 1):
                if i % 4 == 3: #moving to the left
                    x_low -= fib_terms[i]
                    y_low -= fib_terms[i]
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])
                if i % 4 == 0: #moving down
                    y_low -= fib_terms[i]
                    x_hi += fib_terms[i]
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])
                if i % 4 == 1: #moving to the right
                    x_hi += fib_terms[i]
                    y_hi += fib_terms[i]
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])
                if i % 4 == 2: #moving up
                    y_hi += fib_terms[i]
                    x_low -= fib_terms[i]
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])

        return x_low, x_hi, y_low, y_hi

    # produce x & y start and end points for spiral in each successive square \
    # as well as x & y control points for spiral
    def get_spiral_coord(self, n):
        x_zero = []
        y_zero = []
        x_one = []
        y_one = []
        cx_zero = []
        cy_zero = []
        cx_one = []
        cy_one = []

        if n == 0:
            x_zero = []
            y_zero = []
            x_one = []
            y_one = []
            cx_zero = []
            cy_zero = []
            cx_one = []
            cy_one = []

        if n == 1:
            x_zero = [0]
            y_zero = [0]
            x_one = [1]
            y_one = [1]
            cx_zero = [0.5]
            cy_zero = [0]
            cx_one = [1]
            cy_one = [0.5]

        if n == 2:
            x_zero = [0, 1]
            y_zero = [0, 1]
            x_one = [1, 0]
            y_one = [1, 2]
            cx_zero = [0.5, 1]
            cy_zero = [0, 1.5]
            cx_one = [1, 0.5]
            cy_one = [0.5, 2]

        if n == 3:
            x_zero = [0, 1, 0]
            y_zero = [0, 1, 2]
            x_one = [1, 0, -2]
            y_one = [1, 2, 0]
            cx_zero = [0.5, 1, -1]
            cy_zero = [0, 1.5, 2]
            cx_one = [1, 0.5, -2]
            cy_one = [0.5, 2, 1]

        if n == 4:
            x_zero = [0, 1, 0, -2]
            y_zero = [0, 1, 2, 0]
            x_one = [1, 0, -2, 1]
            y_one = [1, 2, 0, -3]
            cx_zero = [0.5, 1, -1, -2]
            cy_zero = [0, 1.5, 2, -1.5]
            cx_one = [1, 0.5, -2, -0.5]
            cy_one = [0.5, 2, 1, -3]

        fib_terms = [0, 1, 1, 2, 3, 5]
        if n >= 5:
            x_zero = [0, 1, 0, -2]
            y_zero = [0, 1, 2, 0]
            x_one = [1, 0, -2, 1]
            y_one = [1, 2, 0, -3]
            cx_zero = [0.5, 1, -1, -2]
            cy_zero = [0, 1.5, 2, -1.5]
            cx_one = [1, 0.5, -2, -0.5]
            cy_one = [0.5, 2, 1, -3]

            for i in range(5, n + 1):
                if i % 4 == 1: # for going to the right
                    x_zero.append(x_one[i - 2])
                    y_zero.append(y_one[i - 2])
                    x_one.append(x_one[i - 2] + fib_terms[i])
                    y_one.append(y_one[i - 2] + fib_terms[i])
                    cx_zero.append(cx_one[i - 2] + fib_terms[i])
                    cy_zero.append(cy_one[i - 2])
                    cx_one.append(x_one[i - 2] + fib_terms[i])
                    cy_one.append(y_one[i - 2] + 0.5 * fib_terms[i])
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])
                if i % 4 == 2: # for going up
                    x_zero.append(x_one[i - 2])
                    y_zero.append(y_one[i - 2])
                    x_one.append(x_one[i - 2] - fib_terms[i])
                    y_one.append(y_one[i - 2] + fib_terms[i])
                    cx_zero.append(x_one[i - 2])
                    cy_zero.append(y_one[i - 2] + 0.5 * fib_terms[i])
                    cx_one.append(x_one[i - 2] - 0.5 * fib_terms[i])
                    cy_one.append(y_one[i - 2] + fib_terms[i])
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])
                if i % 4 == 3: # for going to the left
                    x_zero.append(x_one[i - 2])
                    y_zero.append(y_one[i - 2])
                    x_one.append(x_one[i - 2] - fib_terms[i])
                    y_one.append(y_one[i - 2] - fib_terms[i])
                    cx_zero.append(x_one[i - 2] - 0.5 * fib_terms[i])
                    cy_zero.append(y_one[i - 2])
                    cx_one.append(x_one[i - 2] - fib_terms[i])
                    cy_one.append(y_one[i - 2] - 0.5 * fib_terms[i])
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])
                if i % 4 == 0: # for going down
                    x_zero.append(x_one[i - 2])
                    y_zero.append(y_one[i - 2])
                    x_one.append(x_one[i - 2] + fib_terms[i])
                    y_one.append(y_one[i - 2] - fib_terms[i])
                    cx_zero.append(x_one[i - 2])
                    cy_zero.append(y_one[i - 2] - 0.5 * fib_terms[i])
                    cx_one.append(x_one[i - 2] + 0.5 * fib_terms[i])
                    cy_one.append(y_one[i - 2] - fib_terms[i])
                    fib_terms.append(fib_terms[i - 1] + fib_terms[i])

        return x_zero, y_zero, x_one, y_one, cx_zero, cy_zero, cx_one, cy_one
