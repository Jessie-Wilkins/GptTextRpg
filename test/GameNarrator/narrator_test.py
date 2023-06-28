import pytest
from GptTextRpg.GameWorld.game_map import Room
from GptTextRpg.GameLogic.entities import BasicEntity
from GptTextRpg.GameNarrator.narrator import GameNarrator

def getDescription():
    narrator = GameNarrator()
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
    description = narrator.describe_room(room)
    return description

description = getDescription()

def test_describe_room_can_describe_room_with_all_items():
    assert "vase" in description.lower()

def test_describe_room_can_identify_type_of_room():
    assert "kitchen" in description.lower()

def test_describe_room_can_describe_room_with_all_entities():
    assert "janitor" in description.lower()
