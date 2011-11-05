import re

def intput(str):
    pattern = '''\d+'''
    result = None
    while result is None:
        user_input = input(str)
        result = re.match(pattern, user_input)
    return int(user_input)