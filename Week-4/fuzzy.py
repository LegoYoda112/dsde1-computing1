'''
fuzzy.py

Lint this file using PyLint.
'''

# This function does some maths on three numbers.
def maths(input_a, input_b, input_c):
    """Does some math on the input variables"""
    result = input_a * 3 - input_b + input_c
    return result

# This function returns True or False.
def choices(question):
    """Returns true or false depending on the input"""
    return question

def main():
    """Main method"""
    # first function takes three numbers
    answer = maths(3, 9, 2.3)
    print(answer)

    # second function takes a True or False
    new_answer = choices(True)
    print(new_answer)

if __name__ == '__main__':
    main()
    