import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        yield file.read()

def read_everything(file_path):
    yield from read_file(file_path)
    for line in read_file(file_path):
        yield from read_everything(line)

if __name__ == "__main__":
    for line in read_file("your file path"):
        print(line)