class ThisIsACustomException(Exception):
    pass


sample_dict = {"a": 1}

print(sample_dict)
print(sample_dict["a"])

a = 1
b = 0

try:
    # if b == 0:
    #     raise ThisIsACustomException
    c = a / b
    print("c is:", c)
except KeyError:
    print("we've encountered a key error")
except ZeroDivisionError:
    c = a / 1
    print("entered zero division case")
except ThisIsACustomException:
    print("We've encountered our custom exception")
except Exception as e:
    print("oh no, we've encountered a general exception/error")
finally:
    print("we've reached the finally block")


# print("c:", c)
print("we've made it to the end")
