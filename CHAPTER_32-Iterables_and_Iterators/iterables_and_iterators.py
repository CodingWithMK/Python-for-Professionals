"""
An Iterable is an object that can return an iterator like a list, tuple or a string.
An Iterator is an object that produces the next value in a sequence by calling "next(*object*)" on some object in the iterable.
"""

# ========== Iterable Classes ==========
"""
Iterable classes defiine an __iter__ and __next__ method.
"""


# *TIP*: Every iterator is an iterable, but not every iterable is an iterator.


# Practicing Example

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self): # -> allows iteration like "for x in ..."
        return self  # return itself as an iterator
    
    def __next__(self): # -> delivers the next value in iterable
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1
    
for num in Counter(1, 10):
    print(num)



class EvenNumbers:
    def __init__(self, start, end):
        self.current = start if start % 2 == 0 else start + 1
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current
        self.current += 2
        return val
    
for num in EvenNumbers(4, 12):
    print(num)
    



