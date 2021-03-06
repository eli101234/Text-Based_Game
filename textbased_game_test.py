import pytest
from math import isclose
import board, item , monsters, player
import builtins
from unittest import mock
import unittest                                                                                                                                                                               
import unittest.mock

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
    """
    Does attack_monster method make a player do damage to a monster? What if it
    hurts more than the hp given, will it display a negative?
    """
    test_inventory = board.Inventory()
    test_player = player.Player("Test", "BRUISER", test_inventory)
    monster = monsters.Monsters(1,1,1)
    begin = monster.hp
    test_player.attack_monster(monster)
    end = monster.hp
    #This helps me get just how much damage we randomly did to the monster
    total = begin - end
    #The actual test. Should kill monster, but hp should not show as negative
    captured = capsys.readouterr()
    assert captured.out == (f"Test did {str(total)} damage to the monster!\n"
                            "The monster has 0 hp!\n")
        

def test_attack_player():
    """
    Can the monster attack the player? Does it do damage?
    """
    test_inventory = board.Inventory()
    test_player = player.Player("Test", "WARRIOR", test_inventory)
    monster = monsters.Monsters(30,30,30)
    
    begin_hp = test_player.hp
    monster.attack_player(test_player)
    end_hp = test_player.hp
    #Change of Hp, player got hurt
    assert end_hp < begin_hp


def test_validate_inventory(capsys):
    """Does inventory detect and handle foreign items as expected?"""
    test_category = board.Inventory()
    test_category.inventory['test_potion'] = 12,10,20
    
    #We can place an item in the player inventory
    test_category.show_items()
    captured = capsys.readouterr()
    assert captured.out == ("['test_potion']\n")
    
    #Then use the get_item method to remove the item from the inventory
    test_category.get_item("test_potion")
    test_category.show_items()
    captured = capsys.readouterr()
    assert captured.out == ("[]\n")
    
    

 
