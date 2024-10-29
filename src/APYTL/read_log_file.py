def read_log_file():
    print('Log File Output: \n')
    with open("testresults.log", 'r') as file:
        data = file.read()
    print(data)