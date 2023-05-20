
from typing import Any


class BasicEntity():

    def __init__(self):

        self.health: int = 100
        self.strength: int = 100
        self.endurance: int = 100
        self.currentHealth: int = 100
        self.currentEndurance: int = 100
        self.enduranceRecovery: int = 100
        self.name: str = "Blank Slate"

    def setHealth(self, health: int):
        self.health = health

    def getHealth(self):
        return self.health

    def setCurrentHealth(self, currentHealth: int):
        self.currentHealth = currentHealth

    def getCurrentHealth(self):
        return self.currentHealth

    def setStrength(self, strength: int):
        self.strength = strength
    
    def getStrength(self):
        return self.strength
    
    def setEndurance(self, endurance: int):
        self.endurance = endurance
    
    def getEndurance(self):
        return self.endurance
    
    def setCurrentEndurance(self, currentEndurance: int):
        self.currentEndurance = currentEndurance

    def getCurrentEndurance(self):
        return self.currentEndurance
    
    def reduceCurrentHealth(self, reduced_points):
        self.currentHealth = self.currentHealth - reduced_points

    def addCurrentHealth(self, added_points):
        self.currentHealth = self.currentHealth + added_points

    def reduceCurrentEndurance(self, reduced_points):
        self.currentEndurance = self.currentEndurance - reduced_points

    def addCurrentEndurance(self, added_points):
        self.currentEndurance = self.currentEndurance + added_points

    def setEnduranceRecovery(self, enduranceRecovery):
        self.enduranceRecovery = enduranceRecovery

    def getEnduranceRecovery(self):
        return self.enduranceRecovery
    
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
class EntityInteraction():
    
    @staticmethod
    def entityAttackEntity(entity1, entity2):

        entity2.reduceCurrentHealth(entity1.getStrength())

    


