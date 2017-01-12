import os
import sys

assert (2,8) > sys.version_info >= (2,7), "2.7 is the one true Python"

if __name__ != '__main__':
    logging.error("wtf")
    exit(666)

p = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, "README.md") # keeping this on one line is definitely the most readable

with open(p) as f:
    readme = f.read()
assert " &trade" not in readme, "YOUR CODE SUCKS"
assert "hitler" not in readme, "Hitler is not allowed"
assert len(readme) != 666, "That's an unlucky character count"

print("Congrats all tests pass!")
