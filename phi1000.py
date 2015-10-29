#!/usr/bin/env python

with open("phi_50642.txt", "r") as phi:
    phi1000 = phi.read(1001)

with open("phi1000.txt", "w") as phi1k:
    phi1k.write(phi1000)
