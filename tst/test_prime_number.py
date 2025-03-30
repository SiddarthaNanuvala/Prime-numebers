import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
import prime_number

def test_prime_number_valid():
    # Cas où 7 est un nombre premier
    result = prime_number.is_prime_number(7)
    assert result == True

def test_prime_number_invalid():
    # Cas où 8 n'est pas un nombre premier
    result = prime_number.is_prime_number(8)
    assert result == False

def test_prime_number_edge_case_0():
    # Cas où 0 n'est pas un nombre premier
    result = prime_number.is_prime_number(0)
    assert result == False

def test_prime_number_edge_case_1():
    # Cas où 1 n'est pas un nombre premier
    result = prime_number.is_prime_number(1)
    assert result == False

def test_large_prime():
    # Cas où 9999991 est un nombre premier (test avec un grand nombre)
    result = prime_number.is_prime_number(9999991)
    assert result == True

def test_large_non_prime():
    # Cas où 9999990 n'est pas un nombre premier (test avec un grand nombre non premier)
    result = prime_number.is_prime_number(9999990)
    assert result == False
