class Character:
   '''class character hero'''
   def __init__(self, *data):
      #instance variabel
      self.name = data[0]
      self.hitpoint = data[1]
      self.mana = data[2]

hero1 = Character("Umar", 1000, 500)
hero2 = Character("Nana", 800, 600)
hero3 = Character("Violet", 700, 400)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
