class GameMap:

    def add_room(room):
        return None
        
class Room:
    def __init__(self):
        self.name = "Broom Closet"
        self.entity_list = []
        self.item_list = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def addEntity(self, entity):
        self.entity_list.append(entity)

    def getEntities(self):
        return self.entity_list
    
    def addItem(self, item):
        self.item_list.append(item)

    def getItems(self):
        return self.item_list
        
