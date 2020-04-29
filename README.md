# Unit test your python project with unittest module


1. Create a test directory in the root of your project
2. Create files inside the test directory staring with test_
3. Create class inheriting unittest.TestCase and write methos for testing your code
4. See [Python docs](https://docs.python.org/3/library/unittest.html) For details
5. Run the bellow command to run all the tests

        python -m unittest discover

Run with -v for more verbose
    
        python -m unittest discover -v

Unitest with discover all the test written inside files starting with test_ and class inherited from unittest.TestCase
