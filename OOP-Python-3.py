class Character:
   '''class character hero'''
   #class variabel
   jumlah = 0
   
   #private class variabel
   __cobaPrivate = 0
   #protected class variabel
   _cobaProtected = 0
   def __init__(self, *data):
      #instance variabel
      self.name = data[0]
      self.hitpoint = data[1]
      self.mana = data[2]
      Character.jumlah += 1
      #private variabel
      __varPrivate += 1
      #protected variabel
      _varProtected += 1
   
   #void method
   def say(self):
      print("Hai! Boku wa "+ self.name)
   
   #argument method
   def tambahMana(self,tambahanMana):
      self.mana += tambahanMana
   
   #method return
   def jumlahHitpoint(self):
      return self.hitpoint
       
hero1 = Character("Umar", 1000, 500)
hero2 = Character("Nana", 800, 600)
hero3 = Character("Violet", 700, 400)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

print(f"Jumlah character adalah {Character.jumlah}")
print(f"HP hero1 adalah {hero1.jumlahHitpoint()}")