import pytest
import player
import monsters
from math import isclose

#board py tests
    

def test_attack_monster(capsys):
    test_player = player.Player("Test", "BRUISER")
    monster = monsters.Monster(1,1,1)
    
    test_player.attack_monster(monster)
    captured = capsys.readouterr()
    assert captured.out == ("""
                            Test did {hit} damage to the monster!
                            The monster has 0 hp!
                            """)
    
    
