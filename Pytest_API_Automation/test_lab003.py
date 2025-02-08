# import pytest
# to use mark annotation, need to use  @pytest.mark.smoke
# we can divide testcases using this mark and run them
# to run in the terminal , pytest -m "smoke" path

import pytest
@pytest.mark.smoke
def test_add():
    assert 1 +2 == 3

@pytest.mark.smoke
def test_sub():
    assert 3-2 == 1

@pytest.mark.regression
def test_mul():
    assert 2*2 == 4

@pytest.mark.sanity
def test_div():
    assert 4/2 == 2

