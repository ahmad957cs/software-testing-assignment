import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from login import login

def test_valid_login():
    assert login("admin", "admin123") is True

def test_invalid_password():
    assert login("admin", "wrong") is False

def test_empty_username():
    assert login("", "admin123") is False

def test_empty_password():
    assert login("admin", "") is False

def test_both_empty():
    assert login("", "") is False

def test_invalid_username():
    assert login("user", "admin123") is False
