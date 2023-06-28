from GptTextRpg.GameNarrator.narrator import GameNarrator
from GptTextRpg.GameWorld.game_map import Room
from GptTextRpg.GameLogic.entities import BasicEntity

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

narrator.describe_room(room)