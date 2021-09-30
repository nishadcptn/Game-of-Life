import pytest

import game_of_life

def test_game_repeat():
    _list  = [
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0],
        [0,0,0,0]
    ]

    _list2 = [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert game_of_life.Game(4,4, _list) == _list2
    assert game_of_life.Game(4,4, _list2) == _list


def test_game_constant():
    _list  = [
        [0,1,1,0],
        [1,0,0,1],
        [0,1,1,0],
        [0,0,0,0]
    ]

    assert game_of_life.Game(4,4, _list) == _list

def test_game_normal():
    _list  = [
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0]
    ]

    _list2 = [
        [0, 0, 0, 0], 
        [1, 1, 1, 0], 
        [1, 1, 1, 0], 
        [0, 0, 0, 0]
    ]

    _list3 = [
        [0, 1, 0, 0], 
        [1, 0, 1, 0], 
        [1, 0, 1, 0], 
        [0, 1, 0, 0]
    ]

    assert game_of_life.Game(4,4, _list) == _list2
    assert game_of_life.Game(4,4, _list2) == _list3
    assert game_of_life.Game(4,4, _list3) == _list3


def test_game_4x2():
    _list  = [
        [0,1],
        [0,1],
        [0,1],
        [0,0]
    ]

    _list2 = [
        [0, 0 ],
        [1, 1 ],
        [0, 0 ],
        [0, 0 ]
    ]

    _list3 = [
        [0, 0 ],
        [0, 0 ],
        [0, 0 ],
        [0, 0 ]
    ]

    assert game_of_life.Game(4,2, _list) == _list2
    assert game_of_life.Game(4,2, _list2) == _list3



def test_game_constant():
    _list  = [
        [0,1,1,0],
        [1,0,0,1],
        [0,1,1,0],
        [0,0,0,0]
    ]

    assert game_of_life.Game(4,4, _list) == _list

def test_game_normal():
    _list  = [
        [0,1,0,0,1,1],
        [0,1,0,0,1,0],
        [0,1,0,0,0,1],
        [0,1,0,0,1,0],
        [0,1,0,0,0,1],
        [0,1,0,0,1,0],
    ]

    _list2 = [
        [0, 0, 0, 0, 1, 1], 
        [1, 1, 1, 0, 1, 0], 
        [1, 1, 1, 0, 1, 1], 
        [1, 1, 1, 0, 1, 1], 
        [1, 1, 1, 0, 1, 1], 
        [0, 0, 0, 0, 0, 0]
    ]

    assert game_of_life.Game(6,6, _list) == _list2




    