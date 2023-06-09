import pytest
from GptTextRpg.GameWorld.game_map import Room
from GptTextRpg.GameLogic.entities import BasicEntity
from GptTextRpg.GameNarrator.narrator import GameNarrator

@pytest.fixture(autouse=True)
def room():
    room = Room()
    room.setName("Kitchen")
    entity = BasicEntity()

    entity.setName("Janitor")
    entity.setStrength(50)
    entity.setHealth(50)
    entity.setCurrentEndurance(50)
    entity.setCurrentHealth(50)
    entity.setEnduranceRecovery(50)
    entity.setEndurance(50)
    room.addItem("Vase")

    room.addEntity(entity)
    return room

def test_describe_room_can_describe_room_with_all_items(room):
    narrator = GameNarrator()
    
    description = narrator.describe_room(room)

    assert "Vase" in description
