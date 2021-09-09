from simple import *


def test_1():
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
  

def test_2():
    assert fibo(10) == 55
    assert fibo(1) == 1
    assert fibo(2) == 1
