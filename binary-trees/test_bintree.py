#!/usr/bin/env python3

import bintree


def testBintree(testtree):
    testtree.add_node("test")
    assert testtree.node_exists("test")
    testtree.add_node("foo")
    assert testtree.node_exists("foo")
    assert not testtree.node_exists("bar")


testBintree(bintree.Bintree())
