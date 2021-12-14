# recursion
"""
     in computer science, recursion happens when a functin is called within itself.
     
    
"""


def recursion_(i):
    if i == 1:
        return i
    return recursion_(i - 1)


recursion_(100)
