# Required git config --global --add safe.directory /github/workspace
# Imports (in alphabetically sorted order)
import os
import math


def func1(a, b) -> int:
    return math.floor(a + b)


def func2(a, b, c) -> str:
    return os.getcwd()
