def sum(num1: list, num2):
    # print("-------",type(num1))
    result = num1 + num2
    print("result is ", result)
    return result


output = sum(10, 20)
print(output)

print(sum(10, 20))

print("Type of sum ", type(sum), type(10))

# https://realpython.com/primer-on-python-decorators/

'''
Functions:
============
1.First Class functions
2. Nested Functions
3. Returning Functions
'''


def get_details(abc):
    return abc + 1


def sam(bar):
    print("Output is :", bar + 1)
    return bar + 1


# 1
sam(10)
# 2
print("Function call :", sam(10))
# 3
x = sam(10)
print("Assigned to x :", x)

op = get_details(sam(10))
print("Func call with funtioncall as arg: ", op)

print(sam(2) == 3)  # functions return a value based on the given arguments.

# 1. FIRST CLASS FUNCTIONS:
print("----------1. FIRST CLASS FUNCTIONS------------")


def navn(bar):
    return bar + 1


navn(2)
print(navn(3))
print(type(navn(sam(10 + 20))))
print("Type of foo2 :", type(navn))
print("Function foo2 ", navn)

print("------------------------------------")

'''
Here foo_func requires function name why because 
we have used the same parameter during function call
'''

# function call function_name(arguments)
'''
3 friends - A         B          c     -  1 + 1   
                                          1 - 1   
                                          1+  1    
                                          1   1+
'''


# 1.A
def john(bar):  # foo(10)
    print("---------in foo() function-----------")
    return bar + 1


print("--------------- foo-------------------", foo)
print("--------type of foo-------------------", type(foo))


# 2. B
def call_john_with_arg(john_func, val):
    print("---------in call_foo_with_arg() function-----------")
    res = john_func(val)

    return res  # foo("python")


print("Normal class function call:", john(100))
# 3. C
print("First class function call :", call_john_with_arg(john, 100))  # foo(100) ==> foo  100

print("------------------------------------")
