import pytest
from functions import addition, subtraction, time
from datetime import datetime

def test_addition():
    assert addition (5,5) == 10

def test_subtraction():
    assert subtraction (10,5) == 5

def test_time():
    assert time() == datetime.now()
    