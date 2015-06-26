import module_test
from module_test import hello
from module_test import say

if __name__ == "__main__":
    module_test.hello("Rafael")
    # this hello is diferent for the other hello ;)
    # or not??
    hello()
    # and now??
    say.hello()
