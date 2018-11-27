import unittest

def options_grid_to_list(grid):
    """
    This function turnes a dict of grid values to list of dicts with all
    possible combination of grid values.
    I.e.
    >>> grid = {'option1':['a', 'b', 'c'], 'option2':[10,12,1000]}
    >>> grid_options(grid)
    # Would return
    [
        {'option1': 'a', 'option2': 10},
        {'option1': 'a', 'option2': 12},
        {'option1': 'a', 'option2': 1000},
        {'option1': 'b', 'option2': 10},
        {'option1': 'b', 'option2': 12},
        {'option1': 'b', 'option2': 1000},
        {'option1': 'c', 'option2': 10},
        {'option1': 'c', 'option2': 12},
        {'option1': 'c', 'option2': 1000}
    ]
    """
    options_dicts = [{}]
    for option, values in options_grid.items():
        if not (isinstance(values, tuple) or isinstance(values, list)):
            values = [values,]
        options_dicts = [{**x, **{option:y}} for x in options_dicts for y in values]
    return(options_dicts)

class TestFactorize(unittest.TestCase):
    def basic_test(self):
        grid = {'option1':['a', 'b', 'c'], 'option2':[10,12,1000]}
        ref_list = [
            {'option1': 'a', 'option2': 10},
            {'option1': 'a', 'option2': 12},
            {'option1': 'a', 'option2': 1000},
            {'option1': 'b', 'option2': 10},
            {'option1': 'b', 'option2': 12},
            {'option1': 'b', 'option2': 1000},
            {'option1': 'c', 'option2': 10},
            {'option1': 'c', 'option2': 12},
            {'option1': 'c', 'option2': 1000}
        ]
        with self.subTest(case='basic_test'):
                self.assertEqual(options_grid_to_list(grid), ref_list)

if __name__ == '__main__':
    unittest.main()