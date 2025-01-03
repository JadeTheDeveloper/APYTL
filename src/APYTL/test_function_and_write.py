"""
    params:
    function_to_compare: The fucntion you're testing the output of(This value can or cannot be NULL)
    excpected_value: The value that you are expecting the function to output
    filepath: the file that the completed test will output to, leave as NULL or blank to use the default file(testresults.log)
    function_name: Label's the function that's being tested so it's readable in the logfile.
"""
def test_function_and_write(function_to_compare, expected_value, filepath, function_name):
    f = open("testresults.log", "a")
    if(function_to_compare == expected_value):
        f.write("Tested function: " + str(function_name) + '\n')
        f.write("Expected: " + str(function_to_compare) + '\nGot: ' + str(expected_value) + '\nTest Passed!')
        f.close()
    else:
        f.write("Tested function: " + function_to_compare)
        f.write("Expected: " + str(function_to_compare) + '\nGot: ' + str(expected_value) + '\nTest Failed!')
        f.close()
