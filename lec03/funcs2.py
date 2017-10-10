# funcs2.py
# Diba Mirza
import pytest
import math
# q1 (x1, y1)
#q2  (x2, y2)


def distance2D(q1, q2):
    diffx = q1[0] - q2[0]
    diffy = q1[1] - q2[1]
    return math.sqrt(diffx**2 + diffy**2)

def test_distance2D_0():
    assert(distance2D((0,0), (0,0)) == 0)


def test_distance2D_1():
    assert(distance2D((0,10), (0,20)) == 10)

def test_distance2D_3():
    assert(distance2D((10,0), (0,0)) == 10)

def test_distance2D_4():
    assert(distance2D((0,1), (1,0))**2 == pytest.approx(2))
