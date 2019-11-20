#!/usr/bin/env python3

from mlist import mlist

# These are the test cases for the class.

testlist = mlist()
assert(testlist)

def test_init():
    testlist = mlist()
    assert(testlist)
    assert(testlist.size == 0)
    print("__init__ passed")

def test_getNode():
    testlist = mlist()
    testlist.pushBack("foo")
    testlist.pushBack("bar")
    testlist.pushBack("foobar")
    assert(testlist.getNode(2) == "foobar")
    print("getNode passed")
    
def test_deleteNode():
    testlist = mlist()
    testlist.pushBack("foo")
    assert(testlist.size == 1)
    testlist.deleteNode(0)
    assert(testlist.size == 0)
    print("deleteNode passed")

def test_pushBack():
    testlist = mlist()
    testlist.pushBack("foo")
    testlist.pushBack("bar")
    assert(testlist.getNode(0) == "foo")
    assert(testlist.getNode(1) == "bar")
    assert(testlist.size == 2)
    print("pushBack passed")
    
def test_popBack():
    testlist = mlist()
    testlist.pushBack("foo")
    testlist.pushBack("bar")
    testlist.popBack()
    assert(testlist.size == 1)
    testlist.popBack()
    assert(testlist.size == 0)
    print("popBack passed")
    
test_init()
test_getNode()
test_deleteNode()
test_pushBack()
test_popBack()
print("All tests pass!")
