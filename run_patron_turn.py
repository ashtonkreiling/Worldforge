#!/usr/bin/env python
"""Simple script to run a Patron turn."""
from turns.patron import Patron

if __name__ == "__main__":
    patron = Patron()
    patron.take_turn()

