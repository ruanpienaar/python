#!/usr/bin/env python

def func(arg1, *args, **dict_args):
    print "arg1 was ", arg1
    for a in args:
        print "Arg was : %s" % a
    keys = sorted(dict_args.keys())
    for kw in keys:
        print kw, ":", dict_args[kw]

func("i was", "going to be ", action="walking down the", place="road", time=" at midnight.")
