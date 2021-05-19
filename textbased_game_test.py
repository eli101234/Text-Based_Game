import pytest
from math import isclose
import board, inventory as inv, monsters, player

#battle test
def test_battle():
    
    game = board.Board()
    monsters = monsters.Monsters()
    test_player = player.Player("Tester", "assassin")

    assert board.battle(test_player, monsters, "Aardvark") == True
    assert board.battle(test_player, monsters, "Aric Bills") == False
