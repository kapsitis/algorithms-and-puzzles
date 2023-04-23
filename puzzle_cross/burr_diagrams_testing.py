import pytest
import burr_diagrams

def test_simple():
    assert 1 == 1

def test_mixing():
    var_before =  [
        ["..",
         "..",
         "..",
         "3."],
        ["..",
         "..",
         "..",
         "3."],
        ["1.",
         "1.",
         "1.",
         "22"]
    ]
    var_expected = [
        ["1.",
         "..",
         ".."],
        ["1.",
         "..",
         ".."],
        ["1.",
         "..",
         ".."],
        ["22",
         "3.",
         "3."]
    ]

    assert burr_diagrams.transpose(var_before) == var_expected