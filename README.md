[![Build Status](https://travis-ci.org/eddmash/print_numbers.svg?branch=master)](https://travis-ci.org/eddmash/print_numbers)

Prints the numbers from 1 to 100. But for multiples of three print "Three"
instead of the number and for the multiples of five print "Five".
For numbers which are multiples of both three and five print "ThreeFive".

Installation
------------
You can install `print_numbers` using pip: 

    pip install git+git://github.com/eddmash/print_numbers.git


Usage
-----
To print numbers:
 
    >>> from print_numbers.main import do_print
    >>> do_print(1, 100)
    
Running Tests
-------------

To run tests for the project run the following command while inside the root directory print_numbers

    py.test tests.py