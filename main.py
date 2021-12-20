def response_to_approacher(name, approaching=True):
    def inner_response(func):
        def wrapper(*args, **kwargs):
            if approaching is True:
                print(f"A {name} is coming")
            else:
                print(f"A {name} is leaving")
            response = func(*args, **kwargs)
            return response

        return wrapper
    return inner_response


def print_hello(func):
    def wrapper(*args, **kwargs):
        print("hello")
        return func(*args, **kwargs)
    return wrapper


@response_to_approacher("milkman", False)
@print_hello
def conjure_sound(sound):
    return sound * 2


return_value = conjure_sound("woof")
print("return_value:", return_value)
