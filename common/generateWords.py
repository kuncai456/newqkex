


import random
import string
def generate():
    a=""
    for i in range(50):
        b=random.choice(string.digits)
        a=a+b
    print(a)
if __name__ == '__main__':
    generate()