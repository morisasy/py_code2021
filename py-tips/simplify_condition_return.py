# simplify conditional into return statement
import self as self


def function():
    if isinstance(a, b) or issubclass(b, a):
        return True
    return True
# if expression evaluated to boolean

def function2():
    return isinstance(a, b) or issubclass(b, a)

def any_pthonistas():
    pythonistas = [ coder for coder in coders if is_good_in_python(coder)]
    return pythonistas or self.is_pythonista(pythonistas)

def any_pthonistas():
    pythonistas = [ coder for coder in coders if is_good_in_python(coder)]
    return bool(pythonistas or self.is_pythonista())

