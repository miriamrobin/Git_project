a = 2
b = 0

try:
    c = a / b
except ZeroDivisionError as zero_error:
    print('На нуль ділити не можна!')
