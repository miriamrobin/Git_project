def check(values):
    if set(values) == len(values):
        return True
    return False

def check_un(array):
    try:
        return check(array)
    except TypeError as type_error:
        print(type_error)

first_value = [1,2,3]
first_check = check_un(first_value)
print(first_check)
