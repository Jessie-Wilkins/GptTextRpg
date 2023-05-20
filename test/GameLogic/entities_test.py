import pytest

from GptTextRpg.GameLogic.entities import BasicEntity, EntityInteraction

@pytest.fixture(autouse=True)
def entity():
    # This code will run before each test
    entity = BasicEntity()
    entity.setHealth(50)
    entity.setStrength(50)
    entity.setEndurance(50)
    entity.setCurrentHealth(50)
    entity.setCurrentEndurance(50)
    entity.setEnduranceRecovery(50)
    entity.setName("Janitor")
    return entity

@pytest.fixture(autouse=True)
def enemy():
    enemy = BasicEntity()
    enemy.setHealth(50)
    enemy.setStrength(50)
    enemy.setEndurance(50)
    enemy.setCurrentHealth(50)
    enemy.setCurrentEndurance(50)
    enemy.setEnduranceRecovery(50)
    enemy.setName("Rat")
    return enemy

def test_that_entities_can_get_health(entity):

    assert entity.getHealth() == 50

def test_that_entities_can_get_strength(entity):
    
    assert entity.getStrength() == 50

def test_that_entities_can_get_endurance(entity):

    assert entity.getEndurance() == 50

def test_that_entities_can_get_current_health(entity):

    assert entity.getCurrentHealth() == 50

def test_that_entities_can_reduce_health(entity):

    entity.reduceCurrentHealth(10)

    assert entity.getCurrentHealth() == 40

def test_that_entities_can_add_health(entity):

    entity.addCurrentHealth(10)

    assert entity.getCurrentHealth() == 60

def test_that_entities_can_get_current_endurance(entity):

    assert entity.getCurrentEndurance() == 50

def test_that_endurance_can_be_reduced(entity):

    entity.reduceCurrentEndurance(10)

    assert entity.getCurrentEndurance() == 40

def test_that_endurance_can_be_added(entity):

    entity.addCurrentEndurance(10)

    assert entity.getCurrentEndurance() == 60

def test_that_entity_can_get_endurance_recovery(entity):

    assert entity.getEnduranceRecovery() == 50

def test_that_entities_can_attack(entity, enemy):

    EntityInteraction.entityAttackEntity(entity, enemy)

    assert enemy.getCurrentHealth() == 0

def test_that_entities_can_get_name(entity):

    assert entity.getName() == "Janitor"