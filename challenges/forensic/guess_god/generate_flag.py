from string import ascii_lowercase as low, digits as dig
import random
import sys

string = low + dig + "{" + "}" + "_"
random.seed(sys.argv[1])
for _ in range(int(sys.argv[2])):
    print(chr(ord(random.choice(string))), end="")