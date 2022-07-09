class Hero:
   __countHero = 0
   
   def __init__(self, *args):
      self.__name = args[0]
      self.__hitpoint = args[1]
      self.__mana = args[2]
      Hero.__countHero += 1
      self.__info = "name : {}, health : {}".format(self.__name, self.__hitpoint)
   
   @property
   def info(self):
      return "name : {}, health : {}".format(self.__name, self.__hitpoint)
   
   @property
   def mana(self):
      pass
   
   @mana.getter
   def mana(self):
      return self.__mana
   
   @mana.setter
   def mana(self, input):
      self.__mana = input
   
   @mana.deleter
   def mana(self):
      self.__mana = None
      
#player
umar = Hero("Umar", 1000, 500)

#game
print(umar.info)
umar.mana = 600
print(umar.mana)

del umar.mana
print(umar.__dict__)