from colorama import Fore


"""
    params:
    function_to_compare: The fucntion you're testing the output of(This value can or cannot be NULL)
    excpected_value: The value that you are expecting the function to output
"""
def test_function_value(function_to_compare, expected_value):
    if(function_to_compare != expected_value):
        print(Fore.RED + 'The function did not return its expected value')
        print(Fore.RED + 'Expected: ' + expected_value)
        print(Fore.RED + 'Function Returned: ' + function_to_compare)
        exit(1)
    if(function_to_compare == expected_value):
        print(Fore.CYAN + 'The function returned its expected value!')
        exit(0)