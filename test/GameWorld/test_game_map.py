import pytest
from GptTextRpg.GameWorld.game_map import Room
from GptTextRpg.GameLogic.entities import BasicEntity

@pytest.fixture(autouse=True)
def room():
    room = Room()
    room.setName("Kitchen")
    return room

def test_that_room_can_get_name(room):

    assert room.getName() == "Kitchen"

def test_that_room_can_get_entities(room):

    entity = BasicEntity()

    entity.setName("Janitor")
    entity.setStrength(50)
    entity.setHealth(50)
    entity.setCurrentEndurance(50)
    entity.setCurrentHealth(50)
    entity.setEnduranceRecovery(50)
    entity.setEndurance(50)

    room.addEntity(entity)

    assert room.getEntities()[0] == entity

def test_that_room_can_get_items(room):

    room.addItem("Vase")
    
    assert room.getItems()[0] == "Vase"

    

    