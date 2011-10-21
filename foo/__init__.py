import sys
print "have foo =", "foo" in sys.modules
try:
    from foo.foo import hello
except ImportError:
    from foo import hello
