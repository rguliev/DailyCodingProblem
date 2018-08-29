"""
This file is example of using unit tests from the unittest module.
The module is standard. You don't have to pip install it.
"""
import unittest


def factorize(x):
    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """

    def get_next_prime(primes_used):
        """
        Helper function to get next prime number. The idea here 
        is to increment last used prime number untill we get one that
        is not a multiple of any of used primes.
        """
        next_prime = primes_used[-1] + 1
        residuals = [next_prime % x for x in primes_used]
        while not all(residuals):
            next_prime += 1
            residuals = [next_prime % x for x in primes_used]
        return next_prime

    if type(x) is not int:
        raise TypeError('Input number must be integer')
    if x < 0:
        raise ValueError('Input number must be positive or zero')
    if x == 0 or x == 1:
        return (x, )

    factors = []
    primes_used = [2]  # To track already checked primes
    residual = x  # Remaining part of x % factors
    current_prime = 2
    while residual > 1:
        assert current_prime <= x, "Archived a prime number greater than input number"
        print("Factors are: %s" % factors)
        print("Primes are: %s" % primes_used)
        print("Resiual is: %d" % residual)
        print("Current prime is: %d" % current_prime)
        print("Residual mod Current prime == %d" % (residual % current_prime))

        if residual % current_prime == 0:
            # Do not update current_prime here because
            # it can be used many times, i.e. like 9 = 3*3*3.
            residual = residual // current_prime
            factors.append(current_prime)
        else:
            print("Changing current prime")
            current_prime = get_next_prime(primes_used)
            print("Now current prime is %d" % current_prime)
            primes_used.append(current_prime)

    return tuple(factors)


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        wrong_type_inputs = ('string', 1.5)
        for x in wrong_type_inputs:
            with self.subTest(case=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        negative_inputs = (-1, -10, -100)
        for x in negative_inputs:
            with self.subTest(case=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        with self.subTest(case='zero'):
            self.assertEqual(factorize(0), (0, ))
        with self.subTest(case='one'):
            self.assertEqual(factorize(1), (1, ))

    def test_simple_numbers(self):
        simple_numbers = (3, 13, 29)
        for x in simple_numbers:
            with self.subTest(case=x):
                self.assertEqual(factorize(x), (x, ))

    def test_two_simple_multipliers(self):
        two_simple_multipliers = ((2, 3), (2, 13), (11, 11))
        for x, y in two_simple_multipliers:
            with self.subTest(case=x * y):
                self.assertEqual(factorize(x * y), (x, y))

    def test_many_multipliers(self):
        many_multipliers = (
            (1001, (7, 11, 13)),
            (9699690, (2, 3, 5, 7, 11, 13, 17, 19)),
        )
        for x, factors in many_multipliers:
            with self.subTest(case=x):
                self.assertEqual(factorize(x), factors)


if __name__ == '__main__':
    unittest.main()