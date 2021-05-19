import pytest
from math import isclose
import board, item , monsters, player
import builtins
from unittest import mock

#battle test
def test_battle():
    """
    Does battle() return true if the player wins and false if they lose?
    """
    test_inventory = board.Inventory()
    test_monsters = monsters.Monsters()
    test_player = player.Player("Tester", "assassin",test_inventory)

    with mock.patch("builtins.input", side_effect=["1"]):
        assert board.battle(test_player, test_monsters, "Aardvark") == True
    with mock.patch("builtins.input", side_effect=["1"]):
        assert board.battle(test_player, test_monsters, "Aric Bills") == False
        
def test_attack_monster(capsys):
    test_inventory = board.Inventory()
    test_player = player.Player("Test", "BRUISER", test_inventory)
    monster = monsters.Monsters(1,1,1)
    hitLow = test_player.power - 5
    test_player.attack_monster(monster)
    captured = capsys.readouterr()
    if hit >= self.power - 5 and hit <= self.power + 5:
        assert captured.out == (f"""
                                Test did {hit} damage to the monster!\nThe monster has 0 hp!
                                """)
        
def test_attack_player():
    test_inventory = board.Inventory()
    test_player = player.Player("Test", "WARRIOR", test_inventory)
    monster = monsters.Monsters(30,30,30)
    begin_hp = test_player.hp
    monster.attack_player(test_player)
    end_hp = test_player.hp
    #Change of Hp
    assert end_hp < begin_hp
