#whithere the internet is OK

import os

def is_on_internet():
    exit_code = os.system('ping www.baidu.com')
    return exit_code
#exit_code 0:yes  or no