#!/usr/bin/env python3
#-*- encoding: utf-8 -*-
import sys


def test_this(*arguments, **keywords):
    print("-"*5)
    if arguments:
        print(type(arguments))
        for arg in arguments:
            print(arg)

    if keywords:
        print(type(keywords))
        keys = sorted(keywords.keys())
        for kw in keys:
            print(type(keywords[kw]))
            print(kw, ":", keywords[kw])

# if inform paramethers
if len(sys.argv) > 1:
    test_this(sys.argv[1])
else:
    test_this("a")
    test_this("b")
    test_this(b={'a': 'b'}, c=[1, 2, 3])
    test_this(a="Rafael Henrique")
    test_this('a', c=[1, 2, 3])
