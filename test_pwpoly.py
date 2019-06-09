#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 02:54:42 2019

@author: rt-2pm2
"""
import numpy as np
from trjgen import trjgen_helpers as tjh
from trjgen import trjgen as tj
from trjgen import pwpoly as pw

np.set_printoptions(precision=6)
np.set_printoptions(suppress=True)

# Polynomial characteristic:  order
ndeg = 7
print('Test with {:d}th order polynomial.'.format(ndeg))

## Waipoints in the flat output space (or dimension 3)
nconstr = 4
print('Number of constraint on the flat output = {:d}.'.format(nconstr))


# Build the constraint matrix
X = np.array([
        [ 0,     1.0,    2.0],
        [ 0,     0.01,   0.0],
        [ 0,   -10.0,    0.0],
        [ 0,   np.nan,   0.0],
        ])

Y = np.array([
        [ 0,   0.0,      0.0],
        [ 0,   0.0,      0.0],
        [ 0,   0.0,      0.0],
        [ 0,   np.nan,   0.0],
        ])

Z = np.array([
        [ 0,   0.0,     -0.2],
        [ 0,   0.0,      0.0],
        [ 0,   0.0,      0.0],
        [ 0,   np.nan,   0.0],
        ])

# Times (Absolute and intervals)
knots = np.array([i for i in range(X.shape[1])])
Dt = knots[1:len(knots)] - knots[0:len(knots)-1]

# Compute the polynomials pieces
(solx, nullx, resx, polysx) = tj.interpolPolys(X, ndeg, knots, True)
(soly, nully, resy, polysy) = tj.interpolPolys(Y, ndeg, knots, True)
(solz, nullz, resz, polysz) = tj.interpolPolys(Z, ndeg, knots, True)

# Instantiate the Piecewise polynomials
ppx = pw.PwPoly(polysx, knots)
ppy = pw.PwPoly(polysy, knots)
ppz = pw.PwPoly(polysz, knots)

# Check (Evaluate polynomial)
tv = np.linspace(0,2,100);
(Xtj, Ytj, Ztj, Wtj) = tjh.TrajFromPW(tv, [0,1,2], pwpolx=ppx, pwpoly=ppy, \
                                        pwpolz=ppz, pwpolw = None)


