def test_one():
    assert ('home', 'work') == ('home', 'work')


def test_two():
    a = 'QA'
    b = 'QC'
    assert a == b

def test_three():

     assert not (1, 1, 2, 3, 5) == (2, 3, 5)