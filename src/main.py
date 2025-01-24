from random import randint as ri
from utils import add_numbers, multiply_numbers

def call_functions():
    a = ri(0, 100)
    b = ri(0, 100)
    print(f"a = {a} and b = {b}")
    print("a + b = {}".format(add_numbers(a, b)))
    print("a * b = {}".format(multiply_numbers(a, b)))

if __name__ == "__main__":
    call_functions()

# commit for stash
# this commit is for the rebase task