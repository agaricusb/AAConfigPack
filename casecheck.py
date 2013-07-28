#!/usr/bin/python

import os

def check(root):
    for name in os.listdir(root):
        if hasLowerName(name, root):
            print name


def hasLowerName(name, root):
    for thisName in os.listdir(root):
        if thisName != name and thisName.lower() == name.lower():
            return True
    return False

if __name__ == "__main__":
    check("config")
