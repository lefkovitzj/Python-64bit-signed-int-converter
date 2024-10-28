# Python-64bit-signed-int-converter

This small project was written as an attempt to better understand how programming languages design data structures, and this was my first, largely-unresearched attempt at implementing a conversion from a Python decimal integer to a binary representation of a 64-bit signed integer. 

<hr>

The `utils.py` file includes 3 functions:
* dec_to_bin64s(dec_int)
> The argument `dec_int` takes a value of type "int". <br>The function returns a value of type "string" of length 64, where the value is a representation of the binary value of a 64-bit signed integer equal to the passed argument `dec_int`.

* bin64s_to_dec(bin_str)
> The argument `bin_str` takes a value of type "string" of length 64 where the value is a representation of the binary value of a 64-bit signed integer.<br>The function returns a value of type "int" equal to the passed argument `bin_str`.

* test_conversion(num_tests) 
> The argument `num_tests` takes a value of type "int". The function has no return, but tests the conversion from decimal integer to 64-bit signed integer binary and then back to decimal integer `num_tests` times, displaying a report via the console.

<hr>

When the `utils.py` file is run, a simple command-line-interface appears, offering the user three options:
* Demo (input "d"): Displays a sample conversion from decimal integer to 64-bit signed integer binary and then back to decimal integer.
* Test (input "t"): Asks for a number of iterations, and then passes that value to `test_conversion`.
* Quit (input "q"): End the application without running the "Demo" or "Test" options.

<br>
