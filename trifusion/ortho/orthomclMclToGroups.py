#!/usr/bin/python2

try:
    from process.error_handling import *
except ImportError:
    from trifusion.process.error_handling import *


def mcl_to_groups(prefix, start_id, infile, outfile, nm=None):

    try:
        start_id = int(start_id)
    except ValueError:
        raise ValueError("StartId is not a number")

    input_file = open(infile, "r")
    out = open(outfile, "w")

    for line in input_file:

        if nm:
            if nm.stop:
                raise KillByUser("")
                return

        out.write(prefix + str(start_id) + ": " + line)
        start_id += 1


__author__ = "Fernando Alves"