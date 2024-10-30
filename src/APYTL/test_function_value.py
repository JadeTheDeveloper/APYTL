from colorama import Fore


"""
    params:
    function_to_compare: The fucntion you're testing the output of(This value can or cannot be NULL)
    excpected_value: The value that you are expecting the function to output
    exit_after_result: ether true or false, determines wheather you want to exit after the test completes
"""
def test_function_value(function_to_compare, expected_value, exit_after_result):
    print('Testing function' + test_function_value.__name__ + '...')
    if(function_to_compare != expected_value):
        print(Fore.RED + 'The function did not return its expected value')
        print(Fore.RED + 'Expected: ' + str(expected_value))
        print(Fore.RED + 'Function Returned: ' + str(function_to_compare))
        print(Fore.RESET)
        if(exit_after_result == True):
            exit(1)
    if(function_to_compare == expected_value):
        print(Fore.CYAN + 'The function returned its expected value!')
        print(Fore.RESET)
        if(exit_after_result == True):
            exit(0)