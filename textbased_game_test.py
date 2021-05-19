import pytest
from math import isclose
import board, items as inv, monsters, player
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
        
def test_attack_monster(capsys):
    
    test_player = player.Player("Test", "BRUISER")
    monster = monsters.Monsters(1,1,1)
    hitLow = test_player.power - 5
    test_player.attack_monster(monster)
    captured = capsys.readouterr()
    if hit >= self.power - 5 and hit <= self.power + 5:
        assert captured.out == (f"""
                                Test did {hit} damage to the monster!\nThe monster has 0 hp!
                                """)
