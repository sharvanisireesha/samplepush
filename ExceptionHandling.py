# Exceptions
# checked Exceptions
# Unchecked Exceptions


# simpledecorator

def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        print(f'Function :{func.__name__}')
        func(*args, **kwargs)
        print('-'
              * 20)
    return inner

# Try,Except,Finally


@outline
def test_one(x, y):
    try:
        z = x/y
        print(f"Result is {z}")
    except:
        # catch block
        print("error")

    finally:
        # clean up code
        print("finished")


test_one(5, 0)

test_one(5, 2)


@outline
def test_two(x, y):
    try:
        # assert
        assert(x > 0)
        assert(y > 0)
    except AssertionError:
        print(f"Failed to assert the values as greater than zero {x}, {y}")
    except TypeError:
        print(f"One of the entered values is not a integer , {x},{y}")
    except Exception as e:
        # catch block
        print(f"exception is caught : {e}")
    else:
        # trusted code
        z = x / y
        print(f"Result is {z}")
    finally:
        # clean up code
        print("finished")


test_two(5, 0)
test_two(5, "a")
test_two('ab', 5)
test_two(5, 2)
test_two(0, 9)

# User defined Exceptions and raising


class UDError(RuntimeError):
   # def __init__(self, *args: object) -> None:
    # super().__init__(*args)cls

    def __init__(self, *args):
        self.args = args


@outline
def test_UDE(qty):
    try:
        if not isinstance(qty, int):
            raise TypeError("Must be an integer")
        if qty < 9:
            raise UDError("The quantity should be more than 9",
                          "please make sure you have more")
    except Exception as e:
        print(f'Exeption is {e.args}')
    finally:
        print("complete")


test_UDE(3)
test_UDE(11)
test_UDE(12.3)
