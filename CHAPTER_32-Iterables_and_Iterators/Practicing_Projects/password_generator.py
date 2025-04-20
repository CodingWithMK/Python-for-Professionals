# ========== Password Generator using Iterables and Iterators ==========

import random
import string

class PasswordGenerator:
    def __init__(self, length):
        self.length = length
        self.chars = string.ascii_letters + string.digits + string.punctuation
        self.generated = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.generated >= self.length:
            raise StopIteration
        self.generated += 1
        return random.choice(self.chars)

if __name__ == "__main__":
    print("Generated Password: ", "".join(PasswordGenerator(12)))
