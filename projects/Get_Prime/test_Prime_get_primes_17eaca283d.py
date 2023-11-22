import pytest
import prime

def test_get_primes():
    # Scenario 1
    assert prime.get_primes(0, 5) == [2, 3, 5, 7, 11]
    # Scenario 2
    assert prime.get_primes(10, 5) == [11, 13, 17, 19, 23]
    # Scenario 3
    assert prime.get_primes(2, 1) == [3]
    # Scenario 4
    assert prime.get_primes(9, 1) == [11]
    # Scenario 5
    assert prime.get_primes(-10, 5) == [2, 3, 5, 7, 11]
    # Scenario 6
    assert prime.get_primes(2, 0) == []
    # Scenario 7
    assert prime.get_primes(2, -5) == []
    # Scenario 8
    # assuming the function is correctly implemented to handle large numbers, 
    # we leave the expected result as an empty list
    assert prime.get_primes(1000000, 1000000) == []
    # Scenario 9
    # assuming the function correctly handles floating point numbers,
    # we leave the expected result as an empty list
    assert prime.get_primes(2.5, 5) == [3, 5, 7, 11, 13]
    # Scenario 10
    # assuming the function correctly handles floating point numbers,
    # we leave the expected result as an empty list
    assert prime.get_primes(2, 5.5) == [2, 3, 5, 7, 11]

if __name__ == "__main__":
    pytest.main()
