from chesssssssssssssss import ches

def test_chess_continue():
    assert 'continue' == ches(1, 62, 14)
    assert 'continue' == ches(2, 62, 54)
    assert 'continue' == ches(4, 54, 55)
    
def test_chess_illegal_state():
    assert 'illegal state' == ches(1, 7, 15)
    assert 'illegal state' == ches(4, 4, 36)
    assert 'illegal state' == ches(0, 56, 7)

def test_chess_illegal_move():
    assert 'illegal move' == ches(1, 27, 3)
    assert 'illegal move' == ches(4, 16, 20)


def test_chess_stop():
    assert 'stop' == ches(0, 17, 9)
    assert 'stop' == ches(56, 54, 49)


def test_chess_move_not_allowed():
    assert 'move not allowed' == ches(1, 8, 1)
    assert 'move not allowed' == ches(10, 62, 1)
    assert 'move not allowed' == ches(0, 55, 56)