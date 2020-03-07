# Box Drawing

Python 3 solution 

A method that draws boxes of a given width/height. Comprehensive unit testing is provided, as well as docstrings to allow autodocumentation and facilitate IDE intellisense.

The solution is split across three modules, detailed below.

## draw_box.py

The main file. Contains the draw_box method, which draws the ASCII box. Performs sanity checking for minimum box size and correct types (we want integer width/height values no less than 2). This makes calls to get_code() which retrieves the Unicode value for each component of the box (i.e. top left, space etc). This is converted to a character before printing and then new lines are inserted where necessary. 

## box_constants.py

Stores Unicode values for box components as constants. The advantage of using unicode constants is avoiding ambiguity: distinct unicode values map to very similar looking characters (such as for vertical and horizontal edges). If strings were hardcoded, someone modifying the code could mistake the similar looking characters, and cause a difficult to explain test failure (for instance if they substituted | for │ or ┃). In many editors these appear very similar, and aren't available on most keyboards, so it's safer to use unicode to avoid ambiguity. 

Constants are placed in a separate file for ease of use across the solution and testing, and to allow modification of box appearance from a single place. 

## test_draw_box.py

Unit testing for draw_box. 

Tests that a box of size (3,5) draws correctly. This makes use of the @patch decorator from unittest's mock class to patch stdout into a StringIO object, the value of which can then be compared with an expected output. This keeps the test interface clean: print() calls don't clutter the test result. 

Input validation is also tested. The solution should raise an appropriate exception for non-integer width/height values, as well as width/height values less than two. 

Unit tests for get_code are also present to confirm the method assigns codes to box components correctly. 

