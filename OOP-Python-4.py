class Hero:
   __countHero = 0
   
   def __init__(self, *args):
      self.__name = args[0]
      self.__hitpoint = args[1]
      self.__mana = args[2]
      Hero.__countHero += 1
   
   #getter
   def getName(self):
      return self.__name
   
   def getHitpoint(self):
      return self.__hitpoint
   
   #get dengan argumen class ataupun var
   @staticmethod
   def getHero():
      return Hero.__countHero
   
   @classmethod
   def getHero2(cls):
      return cls.__jumlah
   
   #setter
   def diserang(self,attack):
      self.__hitpoint -= attack
   
   def bluePotion(self):
      self.mana += 100

#player
umar = Hero("Umar", 1000, 500)
nana = Hero("Nmar", 1000, 500)

#game
print(umar.__dict__)
print("Jumlah hero : " + str(Hero.getHero()))
print(umar.getName())        
umar.diserang(100)
print(umar.getHitpoint())
print("Jumlah hero : " + str(umar.getHero()))