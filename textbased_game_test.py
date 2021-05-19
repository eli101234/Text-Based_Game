import pytest
from math import isclose
import board, inventory as inv, monsters, player
import builtins
from unittest import mock

#battle test
def test_battle():
    
    test_monsters = monsters.Monsters()
    test_player = player.Player("Tester", "assassin")

    with mock.patch("builtins.input", side_effect=["1"]):
        assert board.battle(test_player, test_monsters, "Aardvark") == True
    with mock.patch("builtins.input", side_effect=["1"]):
        assert board.battle(test_player, test_monsters, "Aric Bills") == False
