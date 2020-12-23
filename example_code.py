class ClassWithOneFunction:
    def __init__(self):
        print("ClassWithOneFunction initialization")

    def one_function(self):
        print("one_function stuff")


def example_function_with_no_return():
    print("example_function_with_no_return stuff")


def example_function_with_a_return():
    return "put me inside of a print statement to see this message, like print(example_function_with_a_return())"


def example_function_that_takes_one_argument(argument):
    print("i am showing you my " + str(argument))


def example_function_that_only_accepts_strings(argument: str):
    print("you gave me the string : " + argument)


def main():
    cwof = ClassWithOneFunction()
    cwof.one_function()
    example_function_with_no_return()
    print(example_function_with_a_return())
    example_function_that_takes_one_argument(872734)
    example_function_that_only_accepts_strings("potato")


if __name__ == '__main__':
    main()
