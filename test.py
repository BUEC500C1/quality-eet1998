# References: https://realpython.com/python-testing/ & https://www.tutorialspoint.com/python/assertions_in_python.htm 

import pytest
from arabic2roman import arabic2roman

def test():
    assert arabic2roman(3789) == 'MMMDCCLXXXIX'
    assert arabic2roman(7) == 'VII'
    assert arabic2roman(67) == 'LXVII'
    assert arabic2roman(555) == 'DLV'
    assert arabic2roman(1) == 'I'
    assert arabic2roman(3999) == 'MMMCMXCIX'

if __name__ == "__main__":
    test()