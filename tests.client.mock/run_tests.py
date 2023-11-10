import unittest

if __name__ == "__main__":
    # Define the pattern to match test files
    test_pattern = 'test_*.py'
    
    # Create a test loader
    test_loader = unittest.TestLoader()
    
    # Discover and load all the tests in the tests/ directory
    test_suite = test_loader.discover('./tests', pattern=test_pattern)
    
    # Create a test runner that will run the discovered tests
    test_runner = unittest.TextTestRunner(verbosity=2)
    
    # Run the test suite
    test_runner.run(test_suite)
