#!/usr/bin/env python3

"""Demonstrate scoping"""

count = 0

def show_count():
    print("count = ", count)

def set_count(c):
    # We need to use global in order to avoid variable shadowing
    global count
    count = c

show_count()
set_count(5)
show_count()
