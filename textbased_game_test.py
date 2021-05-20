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

    #battle between player and Aardvark. Player should win and return True
    with mock.patch("builtins.input", side_effect=["1"]):
        assert board.battle(test_player, test_monsters, "Aardvark") == True
    
    #battle between player and Aric. Player should lose and return False
    with mock.patch("builtins.input", side_effect=["1"]):
        assert board.battle(test_player, test_monsters, "Aric Bills") == False
        
def test_attack_monster(capsys):
    test_inventory = board.Inventory()
    test_player = player.Player("Test", "BRUISER", test_inventory)
    monster = monsters.Monsters(1,1,1)
    begin = monster.hp
    test_player.attack_monster(monster)
    end = monster.hp
    #This helps me get just how much damage we randomly did to the monster
    total = begin - end
    #The actual test
    captured = capsys.readouterr()
    assert captured.out == (f"Test did {str(total)} damage to the monster!\n"
                            "The monster has 0 hp!\n")
        

def test_attack_player():
    test_inventory = board.Inventory()
    test_player = player.Player("Test", "WARRIOR", test_inventory)
    monster = monsters.Monsters(30,30,30)
    
    begin_hp = test_player.hp
    monster.attack_player(test_player)
    end_hp = test_player.hp
    #Change of Hp, player got hurt
    assert end_hp < begin_hp

def test_validate_inventory():
    """Does inventory detect and handle foreign items as expected?"""
    test_category = board.Inventory()
    test_category.inventory['test_potion'] = 12,10,20
    inventory_result = test_category.get_item('foreign_name')
    captured = capsys.readouterr()
    assert captured.out == ("we don't have that, try again.\n"
                            "What item?")
    