def test_function_and_write(function_to_compare, expected_value):
    f = open("testresults.log")
    if(function_to_compare == expected_value):
        f.write("Expected: " + str(function_to_compare) + '\nGot: ' + str(expected_value) + '\nTest Passed!')
        f.close()
    else:
        f.write("Expected: " + str(function_to_compare) + '\nGot: ' + str(expected_value) + '\nTest Failed!')
        f.close()
