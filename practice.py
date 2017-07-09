"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".


def hello_world():
    """Prints 'Hello World' to console."""

    print "Hello World"

# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.


def say_hi(name):
    """Takes a name and prints 'Hi <name>' to console."""

    print "Hi", name

# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.


def print_product(int1, int2):
    """Takes two integers and prints product of int1 and int2 to the console."""

    print int1 * int2

# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times


def repeat_string(string, integer):
    """Takes a string and an integer and prints the string that number of times."""

    print string * integer

# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".


def print_sign(integer):
    """Evaluates an integer and prints more than zero, zero, or less than zero."""
    
    if integer > 0:
        print "Higher than 0"
    elif integer < 0:
        print "Lower than 0"
    else:
        print "Zero"

# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.


def is_divisible_by_three(integer):
    """Takes an integer and returns true if divisible by 3, or returns false."""

    return integer % 3 == 0

# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.


def num_spaces(sentence):
    """Takes a sentence and returns the number of spaces."""

    spaces = 0

    for char in sentence:
        if char == " ":
            spaces += 1

    return spaces

# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.


def total_meal_price(meal_price, percent_tip=.15):
    """Takes a meal price and tip percentage and returns the total cost of the
    meal with tip. If no tip is given, the default tip is 15 percent."""

    return meal_price + meal_price * percent_tip

# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.


def sign_and_parity(integer):
    """Takes an integer and creates a list indicating whether the integer is
    positive or negative, and whether it is even or odd."""

    integer_sign_parity_list = []

    if integer < 0:
        integer_sign_parity_list.append("Negative")
    elif integer > 0:
        integer_sign_parity_list.append("Positive")
    else:
        integer_sign_parity_list.append("Zero")  # Zero can be n/either, so ??

    if integer % 2 == 0:
        integer_sign_parity_list.append("Even")
    else:
        integer_sign_parity_list.append("Odd")

    return integer_sign_parity_list


integer_info = sign_and_parity(-9)

sign, parity = integer_info

print sign
print parity


###############################################################################

# PART TWO

# 1. Write a function that takes a name and a job title as parameters, making
#    it so the job title defaults to "Engineer" if a job title is not passed
#    in. Return the person's title and name in one string.


def full_title(name, title="Engineer"):
    """Takes a name and job title and returns 'name, title' as one string. If no
    title is given, uses 'Engineer' as default. """

    return title + " " + name


# 2. Given a recipient name & job title and a sender name, print the following
#    letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


def write_letter(name, title, sender):

    print ("Dear " + full_title(name, title) + ", I think you are amazing! "
           + "Sincerely, " + sender)


###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
