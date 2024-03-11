import sys
from io import StringIO
from contextlib import redirect_stdout
import os

os.environ["IS_TESTING"] = "1"

dune = None

null_strIO = StringIO()
sys_stdin = sys.stdin
with redirect_stdout(null_strIO):
    buff = StringIO()
    buff.write("1\n")
    buff.write("A04\n")
    buff.write("a\n")
    buff.seek(0)
    sys.stdin = buff
    dune = __import__("Atelier-2-DUNE-FINAL")
sys.stdin = sys_stdin

turns = ["●", "○"]

def assert_tuple(tupleA, tupleB, len):
    for i in range(0, len):
        # print("TupleA", tupleA[i], " TupleB", tupleB[i])
        assert(tupleA[i] == tupleB[i])

def dummy_system_function(cmd):
    pass

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
        lines, cols = dune.saisir_coordonnees(dune.grille_start)
    
    strIn.close()
    sys.stdin = original_stdin

    return (lines, cols)

def tests_convertor():
    assert_tuple(test_convertor("A04"), (3, 0), 2)

def format_check(coord, grille):
    system_function = os.system
    os.system = dummy_system_function
    res = None
    with redirect_stdout(None):
        res = dune.est_au_bon_format(coord, grille)
    os.system = system_function
    return res

def tests_formats():
    assert not format_check("A41", dune.grille_start)
    assert not format_check("A410", dune.grille_start)
    assert format_check("A04", dune.grille_start)

def not_oob_check(line, col, grille):
    system_function = os.system
    os.system = dummy_system_function
    res = None
    with redirect_stdout(None):
        res = dune.est_dans_grille(line, col, grille)
    os.system = system_function
    return res

def tests_not_oob():
    assert not not_oob_check(100, 100, dune.grille_start)
    assert not_oob_check(0, 0, dune.grille_start)

def test():
    tests_convertor()
    print("Passed tests for 'dune.saisir_coordonnees'")
    tests_formats()
    print("Passed tests for 'dune.est_au_bon_format'")
    tests_not_oob()
    print("Passed tests for 'dune.est_dans_grille'")
    print("Successfully passed all tests !")

if __name__ == "__main__":
    test()