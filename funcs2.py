# funcs2.py
# Diba Mirza
import pytest

def distance2D(q1, q2):
    return 42

def test_distance2D_0():
    assert(distance2D((0,0), (0,0)) == 0)


def test_distance2D_1():
    assert(distance2D((0,10), (0,20)) == 10)

def test_distance2D_3():
    assert(distance2D((10,0), (0,0)) == 10)
