import sys
from io import StringIO
from contextlib import redirect_stdout
import os

os.environ["IS_TESTING"] = "1"

dune = __import__("Atelier-2-DUNE")

turns = ["●", "○"]

def test_convertor(input: str):
    strIn = StringIO()
    strIn.write(input)
    strIn.seek(0)

    original_stdin = sys.stdin
    sys.stdin = strIn
    lines = 0
    cols = 0

    stdout = StringIO()
    with redirect_stdout(stdout):
        lines, cols = dune.saisir_coordonnees(dune.grille_start, turns[0])
    
    strIn.close()
    sys.stdin = original_stdin

    return (lines, cols)

def assert_tuple(tupleA, tupleB, len):
    for i in range(0, len):
        # print("TupleA", tupleA[i], " TupleB", tupleB[i])
        assert(tupleA[i] == tupleB[i])

def tests_convertor():
    assert_tuple(test_convertor("A04"), (3, 0), 2)

def test():
    tests_convertor()
    print("Passed test for 'dune.saisir_coordonnees'")
    # test_formats()

if __name__ == "__main__":
    test()