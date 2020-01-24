#!/usr/bin/python3

import sys
import pprint

from os import getcwd

print("")
print("sys.modules")
pprint.pprint(sys.modules)

print("")
print("sys.path")
pprint.pprint(sys.path)

print("")
print("getcwd()")
print(getcwd())


print("")
print("dir()")

print(dir())

