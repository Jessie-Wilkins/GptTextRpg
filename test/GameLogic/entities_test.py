import pytest

from GptTextRpg.GameLogic.entities import BasicEntity

@pytest.fixture(autouse=True)
def entity():
    # This code will run before each test
    entity = BasicEntity()
    return entity

def test_that_entities_can_get_health(entity):

    entity.setHealth(50)

    assert entity.getHealth() == 50

def test_that_entities_can_get_strength(entity):

    entity.setStrength(50)
    
    assert entity.getStrength() == 50

def test_that_entities_can_get_endurance(entity):

    entity.setEndurance(50)

    assert entity.getEndurance() == 50

def test_that_entities_can_attack(entity):

    entity.setStrength(50)

    assert entity.attack() == 50

def test_that_entities_can_get_current_health(entity):
    entity.setCurrentHealth(50)

    assert entity.getCurrentHealth() == 50

def test_that_entities_can_reduce_health(entity):
    entity.setCurrentHealth(50)

    entity.reduceCurrentHealth(10)

    assert entity.getCurrentHealth() == 40

def test_that_entities_can_add_health(entity):
    entity.setCurrentHealth(50)

    entity.addCurrentHealth(10)

    assert entity.getCurrentHealth() == 60

def test_that_entities_can_get_current_endurance(entity):
    entity.setCurrentEndurance(50)

    assert entity.getCurrentEndurance() == 50

def test_that_endurance_can_be_reduced(entity):
    entity.setCurrentEndurance(50)

    entity.reduceCurrentEndurance(10)

    assert entity.getCurrentEndurance() == 40

def test_that_endurance_can_be_added(entity):
    entity.setCurrentEndurance(50)

    entity.addCurrentEndurance(10)

    assert entity.getCurrentEndurance() == 60

def test_that_entity_can_get_endurance_recovery(entity):
    entity.setEnduranceRecovery(50)

    assert entity.getEnduranceRecovery() == 50