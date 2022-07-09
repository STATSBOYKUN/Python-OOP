class Hero():
   def __init__(self, *args):
      self.__name = args[0]
      self.__hitpoint = args[1]
      self.__mana = args[2]
   
   #getter
   def getName(self):
      return self.__name
   
   def getHitpoint(self):
      return self.__hitpoint
   
   #setter
   def diserang(self,attack):
      self.__hitpoint -= attack
   
   def bluePotion(self):
      self.mana += 100

umar = Hero("Umar", 1000, 500)

#game
print(umar.__dict__)
print(umar.getName())        
hero.diserang(100)
print(umar.getHitpoint())