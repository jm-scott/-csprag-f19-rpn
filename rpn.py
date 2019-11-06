#!/usr/bin/env python3
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '^': operator.pow,
}


def calculate(string: str) -> int:
    stack = list()
    for token in string.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            try:
                function = operator.__dict__[token]
            except KeyError:
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)

    print(stack)
    if len(stack) != 1:
        raise TypeError('Malformed input: ' + string)
    return stack.pop()


def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__':
    main()
