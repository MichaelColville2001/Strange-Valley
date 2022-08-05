import random
main = None
class none:
  def __init__(self,name,slots):
    self.name = name
    self.slots = slots
  

class food:
    def __init__(self, name, desc, heal, slots, price):
      self.name = name
      self.desc = desc
      self.heal = heal
      self.slots = slots
      self.price = price

    def desc():
      print(food.desc)

      
class armor:
    def __init__(self ,name ,desc ,weight ,slots, def_range, price):
      self.name = name
      self.desc = desc
      self.def_range = def_range
      self.weight = weight
      self.slots = slots
      self.price = price

    def desc():
      print(armor.desc)
      
class weapon:
    def __init__(self ,name , desc, weight, at ,hev_at ,slots, price):
      self.name = name
      self.desc = desc
      self.at = at
      self.hev_at = hev_at
      self.weight = weight
      self.slots = slots
      self.price = price
      # sheilds normal atack is block hev at is bash
  
    def desc():
      print(weapon.desc)

  #def call_inventory(self):
    #none item
s = none('',slots=['helm','chest','legs','boots','gloves','r_h','l_h','bag1','bag2','bag3'])


    #foods
apple = food('apple',"come on man it's an apple",heal=[1,2],slots=['bag1','bag2','bag3'],price=[1,2])  
raw_trout = food('raw trout','a raw river fish',heal=[-1,1],slots=['bag1','bag2','bag3'],price=[1,2])
raw_salmon = food('raw salmon','a raw salmon',heal=[-1,2],slots=['bag1','bag2','bag3'],price=[2,3])
raw_rabbit = food('raw rabbit', 'a raw rabbit',heal=[-1,1],slots=['bag1','bag2','bag3'],price=[1,2])
raw_boar = food('raw boar', 'raw boar meat',heal=[-2,1],slots=['bag1','bag2','bag3'],price=[2,3])
raw_venison = food('raw venison','raw venison',heal=[-1,2],slots=['bag1','bag2','bag3'],price=[4,6])
raw_dragon = food('raw dragon meat','a peice of a recently killed dragon',heal=[0,4],slots=['bag1','bag2','bag3'],price=[20,35])
cooked_trout = food('cooked trout','a cooked river fish',heal=[2,3],slots=['bag1','bag2','bag3'],price=[2,3])
cooked_salmon = food('cooked salmon','a cooked salmon',heal=[3,5],slots=['bag1','bag2','bag3'],price=[4,6])
cooked_rabbit = food('cooked rabbit', 'a cooked rabbit',heal=[2,3],slots=['bag1','bag2','bag3'],price=[2,3])
cooked_boar = food('cooked boar', 'cooked boar meat',heal=[3,5],slots=['bag1','bag2','bag3'],price=[4,6])
cooked_venison = food('cooked venison','cooked venison',heal=[5,8],slots=['bag1','bag2','bag3'],price=[9,12])
cooked_dragon = food('cooked dragon meat','cooked dragon meat',heal=[8,12],slots=['bag1','bag2','bag3'],price=[50,60])


    #weapons
stick = weapon('stick','a branch', 1 , at=[1,0] , hev_at=[2,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[0,1])
stone = weapon('stone','a large grey rock',3, at=[2,0], hev_at=[3,0], slots=['r_h','l_h','bag1','bag2','bag3'],price=[0,1])

copper_dagger = weapon('copper dagger','', 1 , at=[1,0] , hev_at=[3,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[2,4])
copper_sword = weapon('copper sword','', 2 , at=[2,0] , hev_at=[4,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[3,5])
copper_mace = weapon('copper mace','', 3 , at=[3,0] , hev_at=[5,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[5,7])
bronze_dagger = weapon('bronze dagger','', 2 , at=[2,0] , hev_at=[4,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[5,7])
bronze_sword = weapon('bronze sword','', 3 , at=[3,0] , hev_at=[5,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[7,10])
bronze_mace = weapon('bronze mace','', 4 , at=[4,0] , hev_at=[7,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[9,12])
iron_dagger = weapon('iron dagger','',  3, at=[3,0] , hev_at=[5,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[9,12])
iron_sword = weapon('iron sword','', 4 , at=[5,0] , hev_at=[8,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[12,16])
iron_mace = weapon('iron mace','',  5, at=[6,0] , hev_at=[10,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[20,25])
voidstone_dagger = weapon('voidstone dagger','', 5 , at=[6,0] , hev_at=[9,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[44,50])
voidstone_sword = weapon('voidstone sword','', 7 , at=[9,0] , hev_at=[13,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[55,65])
voidstone_mace = weapon('voidstone mace','', 10 , at=[12,0] , hev_at=[16,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[70,80])
dragonbone_dagger = weapon('dragonbone dagger','', 3 , at=[7,0] , hev_at=[10,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[80,100])
dragonbone_sword = weapon('dragonbone sword','', 5 , at=[11,0] , hev_at=[14,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[110,130])
dragonbone_mace = weapon('dragonbone mace','',  7, at=[13,0] , hev_at=[15,0] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[140,160])

    #sheild 
wood_sheild = weapon('wood sheild','', 1 , at=[0,1] , hev_at=[0,1] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[2,3])
bronze_sheild = weapon('bronze sheild','', 2 , at=[0,2] , hev_at=[0,2] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[9,12])
iron_sheild = weapon('iron sheild','', 3 , at=[0,3] , hev_at=[0,3] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[25,30])
voidstone_sheild = weapon('voidstone sheild','', 5 , at=[0,4] , hev_at=[0,4] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[69,75])
dragonscale_sheild = weapon('dragonscale sheild','', 3 , at=[0,5] , hev_at=[0,5] , slots=['r_h','l_h','bag1','bag2','bag3'],price=[125,140])

    #armor
       #helm
leather_cap = armor('leather cap', 'a rabbit leather hat', 1, slots=['helm','bag1','bag2','bag3'],def_range=[0,1],price=[2,4])
bronze_helm = armor('bronze helm','',2,slots=['helm','bag1','bag2','bag3'],def_range=[0,2],price=[7,10])
iron_helm = armor('iron helm','',3,slots=['helm','bag1','bag2','bag3'],def_range=[0,4],price=[20,25])
voidstone_helm = armor('voidstone helm','',5,slots=['helm','bag1','bag2','bag3'],def_range=[0,8],price=[40,50])
dragonscale_helm = armor('dragonscale helm','',3,slots=['helm','bag1','bag2','bag3'],def_range=[0,6],price=[80,100])

       #chest
shirt = armor('shirt','a cloth shirt',0,slots=['chest','bag1','bag2','bag3'],def_range=[0,0],price=[0,1])

hide_shirt = armor('hide shirt','',1,slots=['chest','bag1','bag2','bag3'],def_range=[0,4],price=[7,10])
bronze_chestplate = armor('bronze chestplate','',2,slots=['chest','bag1','bag2','bag3'],def_range=[0,8],price=[20,25])
iron_chestplate = armor('iron chestplate','',3,slots=['chest','bag1','bag2','bag3'],def_range=[0,16],price=[40,50])
voidstone_chestplate = armor('voidstone chestplate','',5,slots=['chest','bag1','bag2','bag3'],def_range=[0,32],price=[80,100])
dragonscale_chestplate = armor('dragonscale chestplate','',3,slots=['chest','bag1','bag2','bag3'],def_range=[0,24],price=[160,200]) 

       #legs
pants = armor('pants','cloth pants',0,slots=['legs','bag1','bag2','bag3'],def_range=[0,0],price=[0,1])

hide_pants = armor('hide_pants','',1,slots=['legs','bag1','bag2','bag3'],def_range=[0,3],price=[5,7])
bronze_platelegs = armor('bronze platelegs','',2,slots=['legs','bag1','bag2','bag3'],def_range=[0,6],price=[16,20])
iron_platelegs = armor('iron platelegs','',3,slots=['legs','bag1','bag2','bag3'],def_range=[0,12],price=[35,40])
voidstone_platelegs = armor('voidstone platelegs','',5,slots=['legs','bag1','bag2','bag3'],def_range=[0,24],price=[65,80])
dragonscale_platelegs = armor('dragonscale platelegs','',3,slots=['legs','bag1','bag2','bag3'],def_range=[0,18],price=[140,160])

       #boots
shoes = armor('shoes','basic shoes',0,slots=['boots','bag1','bag2','bag3'],def_range=[0,0],price=[0,1])

hide_boots = armor('hide boots','',1,slots=['boots','bag1','bag2','bag3'],def_range=[0,1],price=[2,4])
bronze_boots = armor('bronze boots','',2,slots=['boots','bag1','bag2','bag3'],def_range=[0,2],price=[7,10])
iron_boots = armor('iron boots','',3,slots=['boots','bag1','bag2','bag3'],def_range=[0,4],price=[20,25])
voidstone_boots = armor('voidstone boots','',5,slots=['boots','bag1','bag2','bag3'],def_range=[0,8],price=[40,50])
dragonscale_boots= armor('dragonscale boots','',3,slots=['boots','bag1','bag2','bag3'],def_range=[0,6],price=[80,100])

       #gloves
hide_gloves = armor('hide gloves','',1,slots=['gloves','bag1','bag2','bag3'],def_range=[0,1],price=[2,4])
bronze_gauntlets = armor('bronze gauntlets','',2,slots=['gloves','bag1','bag2','bag3'],def_range=[0,2],price=[7,10])
iron_gauntlets = armor('iron gauntlets','',3,slots=['gloves','bag1','bag2','bag3'],def_range=[0,4],price=[20,25])
voidstone_gauntlets = armor('voidstone gauntlets','',5,slots=['gloves','bag1','bag2','bag3'],def_range=[0,8],price=[40,50])
dragonscale_gauntlets = armor('dragonscale gauntlets','',3,slots=['gloves','bag1','bag2','bag3'],def_range=[0,6],price=[80,100])


def check(item,item2): #object then slot
  for i in item.slots:
    if i == item2:
      return True
  else:
    print('\nnon compatible\n')


bank = [s,s,s]

def check_bank():
  print(f""" 
      CHEST 1

      {bank[0].name}


      CHEST 2

      {bank[1].name}


      CHEST 3

      {bank[2].name}
      """)
  
class player:
  def __init__(self, name, agility=[1,1], hp=[1,1], strength=1, gp=0, helm=s, chest=shirt, gloves=s, legs=pants, boots=shoes, r_h=s, l_h=s, bag=[s,s,s], score=0, points=10, lvl=[0,1], location=1):
    #name
    self.name = name
    #stats
    self.agility = agility
    self.strength = strength
    self.hp = hp
    #inventory
    self.gp = gp
    self.helm = helm
    self.chest = chest
    self.gloves = gloves
    self.legs = legs
    self.boots = boots
    self.r_h = r_h
    self.l_h = l_h
    self.bag = bag
    #extras
    self.points = points
    self.lvl = lvl
    self.score = score
    self.location = location
    
  def change_hp(self,num):
    self.hp[0] += num

  def item_weight(self,item):
    if item == "helm":
      if Player.helm == s:
        return 0
      else:
        return Player.helm.weight
    elif item == 'chest':
      if Player.chest == s:
        return 0
      else:
        return Player.chest.weight
    elif item == 'legs':
      if Player.legs == s:
        return 0
      else:
        return Player.legs.weight
    elif item == 'boots':
      if Player.boots == s:
        return 0
      else:
        return Player.boots.weight
    elif item == 'gloves':
      if Player.gloves == s:
        return 0
      else:
        return Player.gloves.weight

  def item_def1(self,item):
    if item == "helm":
      if Player.helm == s:
        return 0
      else:
        return Player.helm.def_range[0]
    elif item == 'chest':
      if Player.chest == s:
        return 0
      else:
        return Player.chest.def_range[0]
    elif item == 'legs':
      if Player.legs == s:
        return 0
      else:
        return Player.legs.def_range[0]
    elif item == 'boots':
      if Player.boots == s:
        return 0
      else:
        return Player.boots.def_range[0]
    elif item == 'gloves':
      if Player.gloves == s:
        return 0
      else:
        return Player.gloves.def_range[0]
        
  def item_def2(self,item):
    if item == "helm":
      if Player.helm == s:
        return 0
      else:
        return Player.helm.def_range[1]
    elif item == 'chest':
      if Player.chest == s:
        return 0
      else:
        return Player.chest.def_range[1]
    elif item == 'legs':
      if Player.legs == s:
        return 0
      else:
        return Player.legs.def_range[1]
    elif item == 'boots':
      if Player.boots == s:
        return 0
      else:
        return Player.boots.def_range[1]
    elif item == 'gloves':
      if Player.gloves == s:
        return 0
      else:
        return Player.gloves.def_range[1]
  def item_at(self,item):
    if item == "r_h":
      if Player.r_h == s:
        return 0
      else:
        return Player.r_h.at[0]
    elif item == 'l_h':
      if Player.l_h == s:
        return 0
      else:
        return Player.l_h.at[0]

  def get_wep_weight(self,item):
    if item == "r_h":
      if Player.r_h == s:
        return 0
      else:
        return Player.r_h.weight
    elif item == 'l_h':
      if Player.l_h == s:
        return 0
      else:
        return Player.l_h.weight
  def item_hev_at(self,item):
    if item == "r_h":
      if Player.r_h == s:
        return 0
      else:
        return Player.r_h.hev_at[0]
    elif item == 'l_h':
      if Player.l_h == s:
        return 0
      else:
        return Player.l_h.hev_at[0]
  def item_block(self,item):
    if item == "r_h":
      if Player.r_h == s:
        return 0
      else:
        return Player.r_h.at[1]
    elif item == 'l_h':
      if Player.l_h == s:
        return 0
      else:
        return Player.l_h.at[1]
  def item_bash(self,item):
    if item == "r_h":
      if Player.r_h == s:
        return 0
      else:
        return Player.r_h.hev_at[1]
    elif item == 'l_h':
      if Player.l_h == s:
        return 0
      else:
        return Player.l_h.hev_at[1]
        
  def def_1(self):
    return Player.item_def1('helm') + Player.item_def1('chest') + Player.item_def1('legs') + Player.item_def1('boots') + Player.item_def1('gloves')
    
  def def_2(self):
    return Player.item_def2('helm') + Player.item_def2('chest') + Player.item_def2('legs') + Player.item_def2('boots') + Player.item_def2('gloves')
    
  def get_weight(self):
    return Player.item_weight('helm') + Player.item_weight('chest') + Player.item_weight('legs') + Player.item_weight('boots') + Player.item_weight('gloves')
    
    
  def check_inv(self):
    print(f"""
      HELM
      
      {Player.helm.name}



      CHEST
      
      {Player.chest.name}



      LEGS
      
      {Player.legs.name}


      
      BOOTS
      
      {Player.boots.name}


      
      GLOVES
      
      {Player.gloves.name}


      
      RIGHT HAND
      
      {Player.r_h.name}


      
      LEFT HAND
      
      {Player.l_h.name}


      
      BAG SLOT ONE
      
      {Player.bag[0].name}


      
      BAG SLOT TWO
      
      {Player.bag[1].name}


      
      BAG SLOT THREE
      
      {Player.bag[2].name}



      GOLD PEICES

      {Player.gp}
    """
    )
    
  def call_stats(self):
    print(f'\nlvl: {Player.lvl[1]}\n\n{Player.name} your stats are   hp: {Player.hp[0]}/{Player.hp[1]}   agility: {Player.agility[0]}/{Player.agility[1]}   strength: {Player.strength}\n')


  def switch(self, item1, item2):
    if item1 == 'helm' and (item2 == 'bag1' or item2 == 'bag2' or item2 == 'bag3'):
      if item2 == 'bag1':
        if check(Player.bag[0], 'helm'):
          temp = Player.helm
          Player.helm = Player.bag[0]
          Player.bag[0] = temp
      elif item2 == 'bag2':
        if check(Player.bag[1], 'helm'):
          temp = Player.helm
          Player.helm = Player.bag[1]
          Player.bag[1] = temp
      elif item2 == 'bag3':
        if check(Player.bag[2], 'helm'):
          temp = Player.helm
          Player.helm = Player.bag[2]
          Player.bag[2] = temp
    elif item2 == 'helm' and (item1 == 'bag1' or item1 == 'bag2' or item1 == 'bag3'):
      if item1 == 'bag1':
        if check(Player.bag[0], 'helm'):
          temp = Player.helm
          Player.helm = Player.bag[0]
          Player.bag[0] = temp
      elif item1 == 'bag2':
        if check(Player.bag[1], 'helm'):
          temp = Player.helm
          Player.helm = Player.bag[1]
          Player.bag[1] = temp
      elif item1 == 'bag3':
        if check(Player.bag[2], 'helm'):
          temp = Player.helm
          Player.helm = Player.bag[2]
          Player.bag[2] = temp
          
    elif item1 == 'chest' and (item2 == 'bag1' or item2 == 'bag2' or item2 == 'bag3'):
      if item2 == 'bag1':
        if check(Player.bag[0], 'chest'):
          temp = Player.chest
          Player.chest = Player.bag[0]
          Player.bag[0] = temp
      elif item2 == 'bag2':
        if check(Player.bag[1], 'chest'):
          temp = Player.chest
          Player.chest = Player.bag[1]
          Player.bag[1] = temp
      elif item2 == 'bag3':
        if check(Player.bag[2], 'chest'):
          temp = Player.chest
          Player.chest = Player.bag[2]
          Player.bag[2] = temp
    elif item2 == 'chest' and (item1 == 'bag1' or item1 == 'bag2' or item1 == 'bag3'):
      if item1 == 'bag1':
        if check(Player.bag[0], 'chest'):
          temp = Player.chest
          Player.chest = Player.bag[0]
          Player.bag[0] = temp
      elif item1 == 'bag2':
        if check(Player.bag[1], 'chest'):
          temp = Player.chest
          Player.chest = Player.bag[1]
          Player.bag[1] = temp
      elif item1 == 'bag3':
        if check(Player.bag[2], 'chest'):
          temp = Player.chest
          Player.chest = Player.bag[2]
          Player.bag[2] = temp
          
    elif item2 == 'legs' and (item1 == 'bag1' or item1 == 'bag2' or item1 == 'bag3'):
      if item1 == 'bag1':
        if check(Player.bag[0], 'legs'):
          temp = Player.legs
          Player.legs = Player.bag[0]
          Player.bag[0] = temp
      elif item1 == 'bag2':
        if check(Player.bag[1], 'legs'):
          temp = Player.legs
          Player.legs = Player.bag[1]
          Player.bag[1] = temp
      elif item1 == 'bag3':
        if check(Player.bag[2], 'legs'):
          temp = Player.legs
          Player.legs = Player.bag[2]
          Player.bag[2] = temp
    elif item1 == 'legs' and (item2 == 'bag1' or item2 == 'bag2' or item2 == 'bag3'):
      if item2 == 'bag1':
        if check(Player.bag[0], 'legs'):
          temp = Player.legs
          Player.legs = Player.bag[0]
          Player.bag[0] = temp
      elif item2 == 'bag2':
        if check(Player.bag[1], 'legs'):
          temp = Player.legs
          Player.legs = Player.bag[1]
          Player.bag[1] = temp
      elif item2 == 'bag3':
        if check(Player.bag[2], 'legs'):
          temp = Player.legs
          Player.legs = Player.bag[2]
          Player.bag[2] = temp

    elif item2 == 'boots' and (item1 == 'bag1' or item1 == 'bag2' or item1 == 'bag3'):
      if item1 == 'bag1':
        if check(Player.bag[0], 'boots'):
          temp = Player.boots
          Player.boots = Player.bag[0]
          Player.bag[0] = temp
      elif item1 == 'bag2':
        if check(Player.bag[1], 'boots'):
          temp = Player.boots
          Player.boots = Player.bag[1]
          Player.bag[1] = temp
      elif item1 == 'bag3':
        if check(Player.bag[2], 'boots'):
          temp = Player.boots
          Player.boots = Player.bag[2]
          Player.bag[2] = temp
    elif item1 == 'boots' and (item2 == 'bag1' or item2 == 'bag2' or item2 == 'bag3'):
      if item2 == 'bag1':
        if check(Player.bag[0], 'boots'):
          temp = Player.boots
          Player.boots = Player.bag[0]
          Player.bag[0] = temp
      elif item2 == 'bag2':
        if check(Player.bag[1], 'boots'):
          temp = Player.boots
          Player.boots = Player.bag[1]
          Player.bag[1] = temp
      elif item2 == 'bag3':
        if check(Player.bag[2], 'boots'):
          temp = Player.boots
          Player.boots = Player.bag[2]
          Player.bag[2] = temp

    elif item2 == 'gloves' and (item1 == 'bag1' or item1 == 'bag2' or item1 == 'bag3'):
      if item1 == 'bag1':
        if check(Player.bag[0], 'gloves'):
          temp = Player.gloves
          Player.gloves = Player.bag[0]
          Player.bag[0] = temp
      elif item1 == 'bag2':
        if check(Player.bag[1], 'gloves'):
          temp = Player.gloves
          Player.gloves = Player.bag[1]
          Player.bag[1] = temp
      elif item1 == 'bag3':
        if check(Player.bag[2], 'gloves'):
          temp = Player.gloves
          Player.gloves = Player.bag[2]
          Player.bag[2] = temp
    elif item1 == 'gloves' and (item2 == 'bag1' or item2 == 'bag2' or item2 == 'bag3'):
      if item2 == 'bag1':
        if check(Player.bag[0], 'gloves'):
          temp = Player.gloves
          Player.gloves = Player.bag[0]
          Player.bag[0] = temp
      elif item2 == 'bag2':
        if check(Player.bag[1], 'gloves'):
          temp = Player.gloves
          Player.gloves = Player.bag[1]
          Player.bag[1] = temp
      elif item2 == 'bag3':
        if check(Player.bag[2], 'gloves'):
          temp = Player.gloves
          Player.gloves = Player.bag[2]
          Player.bag[2] = temp

    elif (item1 == 'bag1' or item1 == 'bag2' or item1 == 'bag3') and (item2 == 'bag1' or item2 == 'bag2' or item2 == 'bag3'):
      if item1 == 'bag1':
        if item2 == 'bag2':
          temp = Player.bag[0]
          Player.bag[0] = Player.bag[1]
          Player.bag[1] = temp
        elif item2 == 'bag3':
          temp = Player.bag[0]
          Player.bag[0] = Player.bag[2]
          Player.bag[2] = temp
      elif item1 == 'bag2':
        if item2 == 'bag1':
          temp = Player.bag[0]
          Player.bag[0] = Player.bag[1]
          Player.bag[1] = temp
        elif item2 == 'bag3':
          temp = Player.bag[1]
          Player.bag[1] = Player.bag[2]
          Player.bag[2] = temp
      elif item1 == 'bag3':
        if item2 == 'bag2':
          temp = Player.bag[2]
          Player.bag[2] = Player.bag[1]
          Player.bag[1] = temp
        elif item2 == 'bag1':
          temp = Player.bag[0]
          Player.bag[0] = Player.bag[2]
          Player.bag[2] = temp

    elif item2 == 'rh' and (item1 == 'bag1' or item1 == 'bag2' or item1 == 'bag3'):
      if item1 == 'bag1':
        if check(Player.bag[0], 'r_h'):
          temp = Player.r_h
          Player.r_h = Player.bag[0]
          Player.bag[0] = temp
      elif item1 == 'bag2':
        if check(Player.bag[1], 'r_h'):
          temp = Player.r_h
          Player.r_h = Player.bag[1]
          Player.bag[1] = temp
      elif item1 == 'bag3':
        if check(Player.bag[2], 'r_h'):
          temp = Player.r_h
          Player.r_h = Player.bag[2]
          Player.bag[2] = temp
    elif item1 == 'rh' and (item2 == 'bag1' or item2 == 'bag2' or item2 == 'bag3'):
      if item2 == 'bag1':
        if check(Player.bag[0], 'r_h'):
          temp = Player.r_h
          Player.r_h = Player.bag[0]
          Player.bag[0] = temp
      elif item2 == 'bag2':
        if check(Player.bag[1], 'r_h'):
          temp = Player.r_h
          Player.r_h = Player.bag[1]
          Player.bag[1] = temp
      elif item2 == 'bag3':
        if check(Player.bag[2], 'r_h'):
          temp = Player.r_h
          Player.r_h = Player.bag[2]
          Player.bag[2] = temp

    elif item2 == 'lh' and (item1 == 'bag1' or item1 == 'bag2' or item1 == 'bag3'):
      if item1 == 'bag1':
        if check(Player.bag[0], 'l_h'):
          temp = Player.l_h
          Player.l_h = Player.bag[0]
          Player.bag[0] = temp
      elif item1 == 'bag2':
        if check(Player.bag[1], 'l_h'):
          temp = Player.l_h
          Player.l_h = Player.bag[1]
          Player.bag[1] = temp
      elif item1 == 'bag3':
        if check(Player.bag[2], 'l_h'):
          temp = Player.l_h
          Player.l_h = Player.bag[2]
          Player.bag[2] = temp
    elif item1 == 'lh' and (item2 == 'bag1' or item2 == 'bag2' or item2 == 'bag3'):
      if item2 == 'bag1':
        if check(Player.bag[0], 'l_h'):
          temp = Player.l_h
          Player.l_h = Player.bag[0]
          Player.bag[0] = temp
      elif item2 == 'bag2':
        if check(Player.bag[1], 'l_h'):
          temp = Player.l_h
          Player.l_h = Player.bag[1]
          Player.bag[1] = temp
      elif item2 == 'bag3':
        if check(Player.bag[2], 'l_h'):
          temp = Player.l_h
          Player.l_h = Player.bag[2]
          Player.bag[2] = temp
          
    elif (item1 == 'rh' and item2 == 'lh') or (item2 == 'rh' and item1 == 'lh'):
      temp = Player.r_h
      Player.r_h = Player.l_h
      Player.l_h = temp

  def drop_item(self,item):
    if item == 'helm':
      Player.helm = s
    elif item == 'chest':
      Player.chest = s
    elif item == 'legs':
      Player.legs = s
    elif item == 'boots':
      Player.boots = s
    elif item == 'gloves':
      Player.gloves = s
    elif item == 'rh':
      Player.r_h = s
    elif item == 'lh':
      Player.l_h = s
    elif item == 'bag1':
      Player.bag[0] = s
    elif item == 'bag2':
      Player.bag[1] = s
    elif item == 'bag3':
      Player.bag[2] = s

  def eat(self,item):
    if item == 'bag1':
      is_food = None
      try:
        Player.bag[0].heal[0]
        is_food = True
      except:
        is_food = False
      if is_food:
        heal_amount = random.randint(Player.bag[0].heal[0],Player.bag[0].heal[1])
        if (heal_amount + Player.hp[0]) >= Player.hp[1]:
          Player.hp[0] = Player.hp[1]
          Player.drop_item(item)
          print(f"you healed {heal_amount} hp, your current health is {Player.hp[0]}/{Player.hp[1]}")
        else:
          Player.hp[0] += heal_amount
          Player.drop_item(item)
          print(f"you healed {heal_amount} hp, your current health is {Player.hp[0]}/{Player.hp[1]}")
    if item == 'bag2':
      is_food = None
      try:
        Player.bag[1].heal[0]
        is_food = True
      except:
        is_food = False
      if is_food:
        heal_amount = random.randint(Player.bag[1].heal[0],Player.bag[1].heal[1])
        if (heal_amount + Player.hp[0]) >= Player.hp[1]:
          Player.hp[0] = Player.hp[1]
          Player.drop_item(item)
          print(f"you healed {heal_amount} hp, your current health is {Player.hp[0]}/{Player.hp[1]}")
        else:
          Player.hp[0] += heal_amount
          Player.drop_item(item)
          print(f"you healed {heal_amount} hp, your current health is {Player.hp[0]}/{Player.hp[1]}")
    if item == 'bag3':
      is_food = None
      try:
        Player.bag[2].heal[0]
        is_food = True
      except:
        is_food = False
      if is_food:
        heal_amount = random.randint(Player.bag[2].heal[0],Player.bag[2].heal[1])
        if (heal_amount + Player.hp[0]) >= Player.hp[1]:
          Player.hp[0] = Player.hp[1]
          Player.drop_item(item)
          print(f"you healed {heal_amount} hp, your current health is {Player.hp[0]}/{Player.hp[1]}")
        else:
          Player.hp[0] += heal_amount
          Player.drop_item(item)
          print(f"you healed {heal_amount} hp, your current health is {Player.hp[0]}/{Player.hp[1]}")

  def cook(self):
    Player.check_inv()
    print('\nchoose bag1, bag2, or bag3 to cook that item\n')
    item = input()
    if item == 'bag1':
      if Player.bag[0] == raw_rabbit:
        if random.randint(1,10) > 7:
          Player.bag[0] = s
          print('\nyou burnt the rabbit meat\n')
        else:
          Player.bag[0] = cooked_rabbit
          print('\n you successfully cooked the rabbit meat\n')
      elif Player.bag[0] == raw_trout:
        if random.randint(1,10) > 7:
          Player.bag[0] = s
          print('\nyou burnt the trout\n')
        else:
          Player.bag[0] = cooked_trout
          print('\n you successfully cooked the trout\n')
      elif Player.bag[0] == raw_salmon:
        if random.randint(1,10) > 7:
          Player.bag[0] = s
          print('\nyou burnt the salmon\n')
        else:
          Player.bag[0] = cooked_salmon
          print('\n you successfully cooked the salmon\n')
      elif Player.bag[0] == raw_boar:
        if random.randint(1,10) > 7:
          Player.bag[0] = s
          print('\nyou burnt the boar meat\n')
        else:
          Player.bag[0] = cooked_boar
          print('\n you successfully cooked the boar meat\n')
      elif Player.bag[0] == raw_venison:
        if random.randint(1,10) > 7:
          Player.bag[0] = s
          print('\nyou burnt the venison\n')
        else:
          Player.bag[0] = cooked_venison
          print('\n you successfully cooked the venison\n')
      elif Player.bag[0] == raw_dragon:
        if random.randint(1,10) > 7:
          Player.bag[0] = s
          print('\nyou burnt the dragon meat\n')
        else:
          Player.bag[0] = cooked_dragon
          print('\n you successfully cooked the dragon meat\n')
    elif item == 'bag2':
      if Player.bag[1] == raw_rabbit:
        if random.randint(1,10) > 7:
          Player.bag[1] = s
          print('\nyou burnt the rabbit meat\n')
        else:
          Player.bag[1] = cooked_rabbit
          print('\n you successfully cooked the rabbit meat\n')
      elif Player.bag[1] == raw_trout:
        if random.randint(1,10) > 7:
          Player.bag[1] = s
          print('\nyou burnt the trout\n')
        else:
          Player.bag[1] = cooked_trout
          print('\n you successfully cooked the trout\n')
      elif Player.bag[1] == raw_salmon:
        if random.randint(1,10) > 7:
          Player.bag[1] = s
          print('\nyou burnt the salmon\n')
        else:
          Player.bag[1] = cooked_salmon
          print('\n you successfully cooked the salmon\n')
      elif Player.bag[1] == raw_boar:
        if random.randint(1,10) > 7:
          Player.bag[1] = s
          print('\nyou burnt the boar meat\n')
        else:
          Player.bag[1] = cooked_boar
          print('\n you successfully cooked the boar meat\n')
      elif Player.bag[1] == raw_venison:
        if random.randint(1,10) > 7:
          Player.bag[1] = s
          print('\nyou burnt the venison\n')
        else:
          Player.bag[1] = cooked_venison
          print('\n you successfully cooked the venison\n')
      elif Player.bag[1] == raw_dragon:
        if random.randint(1,10) > 7:
          Player.bag[1] = s
          print('\nyou burnt the dragon meat\n')
        else:
          Player.bag[1] = cooked_dragon
          print('\n you successfully cooked the dragon meat\n')
    elif item == 'bag3':
      if Player.bag[2] == raw_rabbit:
        if random.randint(1,10) > 7:
          Player.bag[2] = s
          print('\nyou burnt the rabbit meat\n')
        else:
          Player.bag[2] = cooked_rabbit
          print('\n you successfully cooked the rabbit meat\n')
      elif Player.bag[2] == raw_trout:
        if random.randint(1,10) > 7:
          Player.bag[2] = s
          print('\nyou burnt the trout\n')
        else:
          Player.bag[2] = cooked_trout
          print('\n you successfully cooked the trout\n')
      elif Player.bag[2] == raw_salmon:
        if random.randint(1,10) > 7:
          Player.bag[2] = s
          print('\nyou burnt the salmon\n')
        else:
          Player.bag[2] = cooked_salmon
          print('\n you successfully cooked the salmon\n')
      elif Player.bag[2] == raw_boar:
        if random.randint(1,10) > 7:
          Player.bag[2] = s
          print('\nyou burnt the boar meat\n')
        else:
          Player.bag[2] = cooked_boar
          print('\n you successfully cooked the boar meat\n')
      elif Player.bag[2] == raw_venison:
        if random.randint(1,10) > 7:
          Player.bag[2] = s
          print('\nyou burnt the venison\n')
        else:
          Player.bag[2] = cooked_venison
          print('\n you successfully cooked the venison\n')
      elif Player.bag[2] == raw_dragon:
        if random.randint(1,10) > 7:
          Player.bag[2] = s
          print('\nyou burnt the dragon meat\n')
        else:
          Player.bag[2] = cooked_dragon
          print('\n you successfully cooked the dragon meat\n')

  def bank(self):
    while True:
      Player.check_inv()
      check_bank()
      print('\npress bag1, bag2, bag3, chest1, chest2, or chest3 to switch that item or [n] to leave\n')
      main = input()
      if main == 'bag1' or main == 'bag2' or main == 'bag3':
        if main == 'bag1':
          print('\npress chest1, chest2, or chest3 to switch that item\n')
          main = input()
          if main == 'chest1':
            temp = Player.bag[0]
            Player.bag[0] = bank[0]
            bank[0] = temp
          elif main == 'chest2':
            temp = Player.bag[0]
            Player.bag[0] = bank[1]
            bank[1] = temp
          elif main == 'chest3':
            temp = Player.bag[0]
            Player.bag[0] = bank[2]
            bank[2] = temp
        elif main == 'bag2':
          print('\npress chest1, chest2, or chest3 to switch that item\n')
          main = input()
          if main == 'chest1':
            temp = Player.bag[1]
            Player.bag[1] = bank[0]
            bank[0] = temp
          elif main == 'chest2':
            temp = Player.bag[1]
            Player.bag[1] = bank[1]
            bank[1] = temp
          elif main == 'chest3':
            temp = Player.bag[1]
            Player.bag[1] = bank[2]
            bank[2] = temp
        elif main == 'bag3':
          print('\npress chest1, chest2, or chest3 to switch that item\n')
          main = input()
          if main == 'chest1':
            temp = Player.bag[2]
            Player.bag[2] = bank[0]
            bank[0] = temp
          elif main == 'chest2':
            temp = Player.bag[2]
            Player.bag[2] = bank[1]
            bank[1] = temp
          elif main == 'chest3':
            temp = Player.bag[2]
            Player.bag[2] = bank[2]
            bank[2] = temp
      elif main == 'chest1' or main == 'chest2' or main == 'chest3':
        if main == 'chest1':
          print('\npress bag1, bag2, or bag3 to switch that item\n')
          main = input()
          if main == 'bag1':
            temp = Player.bag[0]
            Player.bag[0] = bank[0]
            bank[0] = temp
          elif main == 'bag2':
            temp = Player.bag[1]
            Player.bag[1] = bank[0]
            bank[0] = temp
          elif main == 'bag3':
            temp = Player.bag[2]
            Player.bag[2] = bank[0]
            bank[0] = temp
        elif main == 'chest2':
          print('\npress bag1, bag2, or bag3 to switch that item\n')
          main = input()
          if main == 'bag1':
            temp = Player.bag[0]
            Player.bag[0] = bank[1]
            bank[1] = temp
          elif main == 'bag2':
            temp = Player.bag[1]
            Player.bag[1] = bank[1]
            bank[1] = temp
          elif main == 'bag3':
            temp = Player.bag[2]
            Player.bag[2] = bank[1]
            bank[1] = temp
        elif main == 'chest3':
          print('\npress bag1, bag2, or bag3 to switch that item\n')
          main = input()
          if main == 'bag1':
            temp = Player.bag[0]
            Player.bag[0] = bank[2]
            bank[2] = temp
          elif main == 'bag2':
            temp = Player.bag[1]
            Player.bag[1] = bank[2]
            bank[2] = temp
          elif main == 'bag3':
            temp = Player.bag[2]
            Player.bag[2] = bank[2]
            bank[2] = temp
      else:
        break

Player = player(input("\nEnter your name here: "))

class mob:
  def __init__(self,name,desc,l_t,at=[0,0],at_2=[0,0],s_at=[0,0],agility=[0,0],hp=[1,1],strength=[0,0],def_range=[1,1],gp=[0,0],xp=1):
   self.name = name
   self.desc = desc
   self.l_t = l_t
   self.at = at
   self.at_2 = at_2
   self.s_at = s_at
   self.agility = agility
   self.hp = hp
   self.strength = strength
   self.def_range = def_range
   self.gp = gp
   self.xp = xp



    
def one_two(n1,n2):
  list = [n1,n2]
  return list[random.randint(0,1)]


def add_stats():
  while True:
    Player.call_stats()
    if Player.points == 0:
      break
    choice = input(f"You have {Player.points} points left, use [h], [a], [s] to add points to that stat\n\n")
    if choice == 'h':
      Player.points -= 1
      Player.hp[0] +=1
      Player.hp[1] +=1
    elif choice == 'a':
      Player.points -= 1
      Player.agility[0] +=1
      Player.agility[1] +=1
    elif choice == 's':
      Player.points -= 1
      Player.strength +=1

def player_stuff():
  while True:
        if Player.hp[0] <= 0:
          break
        print('\npress inv for inventory,  stats for stats, or m to move on\n')
        main=input()
        if main == 'inv':
            while True:
              if Player.hp[0] <= 0:
                 break
              Player.check_inv()
              print('\npress s to switch items,  d to drop items,  e to eat food,   or m to move on\n')
              main=input()
              if main == 's':
                Player.switch(input('\npress helm, chest, legs, boots, gloves, rh, lh, bag1, bag2,or bag3 to switch that item\n\n'),input('\npress helm, chest, legs, boots, gloves, rh, lh, bag1, bag2,or bag3 to switch that item\n\n'))
              elif main == 'd':
                main = input('\npress helm, chest, legs, boots, gloves, rh, lh, bag1, bag2,or bag3 to drop that item\n\n')
                Player.drop_item(main)
              elif  main == 'e':
                main = input('\npress bag1, bag2, or bag3 to eat that item\n\n')
                Player.eat(main)
              elif main == 'm':
                break
        elif main == 'stats':
            Player.call_stats()
        elif main == 'm':
            break

def L_T(*args): #L_T = Loot Table
  arg = args
  key_list = arg[::2]
  num_list = arg[1::2]
  weighted_list = []
  interator = 0
  for i in key_list:
    for ai in range(num_list[interator]):
      weighted_list.append(i)
    interator += 1
  return weighted_list

def pick_up(item):
    if item == None:
      return item
    print(f'{Player.name} you found a {item.name}!')
    ans = input("\nwould you like to pick it up [y/n]\n")
    if ans == 'y':
      while True:
        ans = input("\nwhat slot would you like to put it in bag1, bag2, bag3, or inv to check inv and [n] to leave?\n")
        if ans == 'bag1':
          if Player.bag[0] == s:
            Player.bag[0] = item
            break
        elif ans == 'bag2':
          if Player.bag[1] == s:
            Player.bag[1] = item
            break
        elif ans == 'bag3':
          if Player.bag[2] == s:
            Player.bag[2] = item
            break
        elif ans == 'inv':
          player_stuff()
        elif ans == 'n':
          break
          

def pick_loot(list):
  pick_up(list[(random.randint(1,len(list))-1)])

   #loot tables
  #places 
common_forest=L_T(None,12,apple,6,stick,2,stone,1) 
uncommon_forest=L_T(None,15,apple,6,copper_sword,1,copper_mace,1,wood_sheild,1,copper_dagger,1)
rare_forest=L_T(None,21,bronze_sheild,1,bronze_dagger,1,bronze_sword,1,bronze_mace,1)

common_dungeon=L_T(None,24,hide_shirt,3,hide_pants,3,hide_boots,3,hide_gloves,3,leather_cap,3,copper_dagger,3,copper_sword,3,copper_mace,3,wood_sheild,3,bronze_helm,1,bronze_platelegs,1,bronze_chestplate,1,bronze_gauntlets,1,bronze_boots,1,bronze_sheild,1,bronze_dagger,1,bronze_sword,1,bronze_mace,1)
uncommon_dungeon=L_T(None,50,iron_helm,3,iron_platelegs,3,iron_chestplate,3,iron_gauntlets,3,iron_boots,3,iron_sheild,3,iron_dagger,3,iron_sword,3,iron_mace,3,voidstone_sheild,1,voidstone_dagger,1,voidstone_sword,1,voidstone_mace,1)
rare_dungeon=L_T(None,50,voidstone_helm,3,voidstone_platelegs,3,voidstone_chestplate,3,voidstone_gauntlets,3,voidstone_boots,3,voidstone_sheild,3,voidstone_dagger,3,voidstone_sword,3,voidstone_mace,3,dragonscale_helm,1,dragonscale_platelegs,1,dragonscale_chestplate,1,dragonscale_gauntlets,1,dragonscale_boots,1,dragonscale_sheild,1,dragonbone_dagger,1,dragonbone_sword,1,dragonbone_mace,1)

  #mob loot tables
rabbit_loot=L_T(None,6,raw_rabbit,5,leather_cap,1)
boar_loot=L_T(None,12,raw_boar,10,hide_boots,1,hide_gloves,1)
elk_loot=L_T(None,12,raw_venison,10,hide_shirt,1,hide_pants,1)

goblin_loot=L_T(None,12,hide_shirt,1,hide_pants,1,hide_boots,1,hide_gloves,1,leather_cap,1,copper_dagger,1,copper_sword,1,copper_mace,1,wood_sheild,1)
skeleton_loot=L_T(None,15,bronze_helm,1,bronze_platelegs,1,bronze_chestplate,1,bronze_gauntlets,1,bronze_boots,1,bronze_sheild,1,bronze_dagger,1,bronze_sword,1,bronze_mace,1)
troll_loot=L_T(None,15,iron_helm,1,iron_platelegs,1,iron_chestplate,1,iron_gauntlets,1,iron_boots,1,iron_sheild,1,iron_dagger,1,iron_sword,1,iron_mace,1)
cyclops_loot=L_T(None,18,voidstone_helm,1,voidstone_platelegs,1,voidstone_chestplate,1,voidstone_gauntlets,1,voidstone_boots,1,voidstone_sheild,1,voidstone_dagger,1,voidstone_sword,1,voidstone_mace,1)
dragon_loot=L_T(raw_dragon,15,dragonscale_helm,1,dragonscale_platelegs,1,dragonscale_chestplate,1,dragonscale_gauntlets,1,dragonscale_boots,1,dragonscale_sheild,1,dragonbone_dagger,1,dragonbone_sword,1,dragonbone_mace,1)

shop_loot=L_T(cooked_dragon,2,raw_dragon,2,dragonscale_helm,1,dragonscale_platelegs,1,dragonscale_chestplate,1,dragonscale_gauntlets,1,dragonscale_boots,1,dragonscale_sheild,1,dragonbone_dagger,1,dragonbone_sword,1,dragonbone_mace,1,voidstone_helm,2,voidstone_platelegs,2,voidstone_chestplate,2,voidstone_gauntlets,2,voidstone_boots,2,voidstone_sheild,2,voidstone_dagger,2,voidstone_sword,2,voidstone_mace,2,iron_helm,4,iron_platelegs,4,iron_chestplate,4,iron_gauntlets,4,iron_boots,4,iron_sheild,4,iron_dagger,4,iron_sword,4,iron_mace,4,bronze_helm,6,bronze_platelegs,6,bronze_chestplate,6,bronze_gauntlets,6,bronze_boots,6,bronze_sheild,6,bronze_dagger,6,bronze_sword,6,bronze_mace,6,hide_shirt,8,hide_pants,8,hide_boots,8,hide_gloves,8,leather_cap,8,copper_dagger,8,copper_sword,8,copper_mace,8,wood_sheild,8,raw_venison,8,cooked_venison,8,raw_boar,10,cooked_boar,10,raw_rabbit,10,cooked_rabbit,10,raw_trout,10,cooked_trout,10,raw_salmon,10,cooked_salmon,10)

  #mobs
rabbit = mob('rabbit','a rabbit',rabbit_loot,at=['scratch',1],at_2=['slash',2],s_at=['bite',3],agility=[0,2],hp=[0,3],strength=[0,1],def_range=[1,2],gp=[1,2],xp=1)
boar = mob('boar','',boar_loot,at=['bite',1],at_2=['tusk',2],s_at=['ram',3],agility=[0,3],hp=[0,5],strength=[0,2],def_range=[4,6],gp=[2,4],xp=5)
elk = mob('elk','',elk_loot,at=['rake',1],at_2=['kick',2],s_at=['charge',3],agility=[0,5],hp=[0,9],strength=[0,3],def_range=[8,10],gp=[5,8],xp=10)

goblin = mob('goblin','',goblin_loot,at=['punch',1],at_2=['slash',2],s_at=['stab',3],agility=[0,7],hp=[0,15],strength=[0,4],def_range=[0,15],gp=[8,15],xp=15)
skeleton = mob('skeleton','',skeleton_loot,at=['punch',1],at_2=['slash',2],s_at=['stab',3],agility=[0,10],hp=[0,12],strength=[0,5],def_range=[0,10],gp=[10,16],xp=20)
troll = mob('troll','',troll_loot,at=['tackle',1],at_2=['bite',2],s_at=['smash',3],agility=[0,15],hp=[0,35],strength=[0,7],def_range=[0,20],gp=[20,35],xp=40)
cyclops = mob('cyclops','',cyclops_loot,at=['stomp',1],at_2=['club',2],s_at=['smash',3],agility=[0,25],hp=[0,50],strength=[0,9],def_range=[0,45],gp=[50,75],xp=70)
dragon = mob('dragon','',dragon_loot,at=['wing slash',1],at_2=['tail swipe',2],s_at=['breath fire',3],agility=[0,50],hp=[0,100],strength=[0,13],def_range=[0,70],gp=[100,200],xp=100)

# = mob('','',,at=['',1],at_2=['',2],s_at=['',3],agility=[0,],hp=[0,],strength=[0,],def_range=[0,],gp=[,],xp=)
  #mob tables
#forest
f1=L_T(None,24,rabbit,8,boar,3,goblin,1)
f2=L_T(None,24,rabbit,6,boar,4,elk,2,goblin,1)
f3=L_T(None,12,boar,3,elk,2,skeleton,1)
f4=L_T(None,300,rabbit,100,boar,60,elk,30,dragon,1)

#dungeon
de=L_T(None,200,goblin,50,skeleton,25,troll,13,cyclops,8,dragon,4)
d1=L_T(None,1,goblin,4,skeleton,1)
d2=L_T(None,1,skeleton,4,troll,1)
d3=L_T(None,1,troll,4,cyclops,1)
d4=L_T(None,1,cyclops,4,dragon,1)



  
def shop(l_t):
  while True:
    main = input('\nyou find a wandering trader, would you like to trade [y/n]\n')
    if main == 'y':
      main = input('\nwould you like to buy or sell [b/s] or leave [n]\n')
      if main == 'b':
         Player.check_inv()
         item = l_t[random.randint(1,len(l_t))-1]
         main = input(f"would you like to buy a {item.name} for {item.price[1]} gp [y/n]")
         if main == 'y' and Player.gp >= item.price[1]:
           Player.check_inv()
           main = input('\nwhere would you like to put it bag1, bag2, or bag3\n')
           if main == 'bag1':
              if Player.bag[0] == s:
                Player.bag[0] = item
                Player.gp -= item.price[1]
                Player.check_inv()
                break
              else:
                break
           elif main == 'bag2':
              if Player.bag[1] == s:
                Player.bag[1] = item
                Player.gp -= item.price[1]
                Player.check_inv()
                break
              else:
               break
           elif main == "bag3":
              if Player.bag[2] == s:
                Player.bag[2] = item
                Player.gp -= item.price[1]
                Player.check_inv()
                break
              else:
               break
         else:
           break
      elif main == 's':
       while True:
        Player.check_inv()
        main = input('\nwhat would you like to sell bag1, bag2, or bag3 or [n] to leave\n')
        if main == 'bag1':
          if Player.bag[0] == s:
            break
          else:
            main = input(f'would you like to sell your {Player.bag[0].name} for {Player.bag[0].price[0]} gp [y/n]')
            if main == 'y':
              Player.gp += Player.bag[0].price[0]
              Player.drop_item('bag1')
        elif main == 'bag2':
          if Player.bag[1] == s:
            break
          else:
            main = input(f'would you like to sell your {Player.bag[1].name} for {Player.bag[1].price[0]} gp [y/n]')
            if main == 'y':
              Player.gp += Player.bag[1].price[0]
              Player.drop_item('bag2')
        elif main == 'bag3':
          if Player.bag[2] == s:
            break
          else:
            main = input(f'would you like to sell your {Player.bag[2].name} for {Player.bag[2].price[0]} gp [y/n]')
            if main == 'y':
              Player.gp += Player.bag[2].price[0]
              Player.drop_item('bag3')
        elif main == 'n':
          break
    if main == 'n':
      break


def add_lvl(lvl,xp1,xp2):
  while True:
    if Player.lvl[1] == lvl and Player.lvl[0] >= xp1:
      print('\nyou leveled up\n')
      Player.points += 1
      Player.lvl[0] -= xp1
      Player.lvl[1] += 1
      add_stats()
      if Player.lvl[0] < xp2:
        break
    else:
      break

def lvls():
  add_lvl(1,10,20)
  add_lvl(2,20,50)
  add_lvl(3,50,80)
  add_lvl(4,80,120)
  add_lvl(5,120,180)
  add_lvl(6,180,260)
  add_lvl(7,260,320)
  add_lvl(8,320,400)
  add_lvl(9,400,500)
  add_lvl(10,500,550)
  add_lvl(11,550,600)
  add_lvl(12,600,700)
  add_lvl(13,700,900)
  add_lvl(14,900,1100)
  add_lvl(15,1100,1300)
  add_lvl(16,1300,1500)
  add_lvl(17,1500,1700)
  add_lvl(18,1700,1850)
  add_lvl(19,1850,2000)
  add_lvl(20,2000,100000)
      


def fight(l_t):
  mob = l_t[random.randint(1,len(l_t))-1]
  if mob == None:
    return None
  lvl = int(Player.lvl[1] * 1.1) + random.randint(0,3)
  
  mob.agility[0] = mob.agility[1]
  mob.hp[0] = mob.hp[1]
  mob.strength[0] = mob.strength[1]
  mob_total = mob.agility[0] + mob.hp[0] + mob.strength[0]
  mob.agility[0] += int((mob.agility[0] / mob_total) * (lvl/3)) + mob.agility[0]
  mob.hp[0] += int((mob.hp[0] / mob_total) * (lvl/3)) + mob.hp[0]
  mob.strength[0] += int((mob.strength[0] / mob_total) * (lvl/3)) + mob.strength[0]

  w1 = Player.def_1()
  w2 = Player.def_2()
  w = Player.get_weight()
  w_w = Player.get_wep_weight('l_h') + Player.get_wep_weight('r_h')
  at =  Player.strength + w_w + Player.item_at('r_h') + Player.item_at('l_h')
  hev_at =  Player.strength + w_w + Player.item_hev_at('r_h') + Player.item_hev_at('l_h')
  bash = Player.item_bash('r_h') + Player.item_bash('l_h')
  block = w_w + Player.item_block('r_h') + Player.item_block('l_h')
  
  print(' ')
  print(f"you come across a lvl {lvl} {mob.name}")
  print(' ')
  while mob.hp[0] > 0 and Player.hp[0] > 0:
    print(f"it has {mob.hp[0]} hp")
    print(' ')
    Player.call_stats()
    print('')
    player_stuff()
    rand = random.randint(1,(Player.agility[0] + mob.agility[0] + w_w))
    if rand > Player.agility[0]:
      mob_at = random.randint(1,10)
      if random.randint(1,10) <= 7:
        p = True
        if mob_at >= 1 and mob_at <= 7:
          print(f"the {mob.name} is preparing to {mob.at[0]}")
        elif mob_at >= 8 and mob_at <= 9:
          print(f"the {mob.name} is preparing to {mob.at_2[0]}")
        elif mob_at == 10:
          print(f"the {mob.name} is preparing to {mob.s_at[0]}")
      else:
        p = False
      attack = input('\npress [at] for a normal atack, [hev] for a heavy atack, [bash], for a bash, [block] to block, [d] to dodge, or [run] to try and run\n')
      if attack == 'at':
        if p:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1])))) + at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1]))))+ at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1]))))+ at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp 
        else:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1]))))+ at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1]))))+ at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1]))))+ at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp 

            
      elif attack == 'hev' and Player.agility[0] > 0:
        if p:
          Player.agility[0] -= 1
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(hev_at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1])))) + hev_at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(hev_at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1])))) + hev_at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(hev_at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1])))) + hev_at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp 
        else:
          Player.agility[0] -= 1
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(hev_at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1])))) + hev_at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(hev_at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1])))) + hev_at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
            if Player.hp[0] <= 0:
              break
            else:
              temp = int(round(hev_at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1])))) + hev_at)
              print(f'you did {temp} damage')
              mob.hp[0] -= temp

        
      elif attack == 'bash' and Player.agility[0] > 0:
        Player.agility[0] -= 1
        if random.randint(1,12) <= bash:
          print(f'you bashed the {mob.name}')
          temp = Player.strength
          print(' ')
          print(f'you did {temp} damage')
          mob.hp[0] -= temp
        else:
         print('\nyou failed your bash\n')
         if p:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]*0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
         else:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp

        
      elif attack == 'block':
       if random.randint(1,12) <= block:
        if p:
          print('\nyou blocked the attack')
        else:
            if mob_at >= 1 and mob_at <= 7:
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
          elif mob_at >= 8 and mob_at <= 9:
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
          elif mob_at == 10:
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
            print('\nyou blocked the attack')
       else:
         print('\nyou failed your block\n')
         if p:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
         else:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          
        
      elif attack == 'd':
        rand = random.randint(1,(Player.agility[0] + mob.agility[0]))
        if (rand + w) <= Player.agility[0]:
          print('you sucsessfuly dodged')
        else:
         print('\nyou failed to dodge\n')
         if p:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
         else:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp

          
      elif attack == 'run':
        rand = random.randint(1,(Player.agility[0] + mob.agility[0]))
        if (rand) <= Player.agility[0]:
          break
        else:
         print('\nyou failed to run\n')
         if p:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
         else:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp

      else:
        if p:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]*0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]*0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]*0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
        else:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]*0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]*0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]*0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
    else:
      mob_at = random.randint(1,10)
      attack = input('\npress [at] for a normal atack, [hev] for a heavy atack, [bash], for a bash, [block] to block, [d] to dodge, or [run] to try and run\n')

      
      if attack == 'at':
        temp = int(round(at - (0.01 * random.randint(mob.def_range[0],mob.def_range[1]))) + at)
        print(f'you did {temp} damage')
        print('')
        mob.hp[0] -= temp
        if mob.hp[0] < 1:
          break
        if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]*0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
            print(f'you took {temp} damage')
            Player.hp[0] -= temp
        elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
            print(f'you took {temp} damage')
            Player.hp[0] -= temp
        elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
            print(f'you took {temp} damage')
            Player.hp[0] -= temp

          
      elif attack == 'hev' and Player.agility[0] > 0:
        temp = int(round(hev_at - ((0.01 * random.randint(mob.def_range[0],mob.def_range[1])))) + hev_at)
        print(f'you did {temp} damage')
        print('')
        Player.agility[0] -= 1
        mob.hp[0] -= temp
        if mob.hp[0] < 1:
          break
        if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
            print(f'you took {temp} damage')
            Player.hp[0] -= temp
        elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
            print(f'you took {temp} damage')
            Player.hp[0] -= temp
        elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
            print(f'you took {temp} damage')
            Player.hp[0] -= temp     
      elif attack == 'bash' and Player.agility[0] > 0:
        Player.agility[0] -= 1
        if random.randint(1,12) <= bash:
          print(f'you bashed the {mob.name}')
          temp = Player.strength
          print(' ')
          print(f'you did {temp} damage')
          mob.hp[0] -= temp
        else:
         print('\nyou failed your bash\n')
         if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
         elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
         elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
        
      elif attack == 'block':
        if random.randint(1,12) <= block:
          if mob_at >= 1 and mob_at <= 7:
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
          elif mob_at >= 8 and mob_at <= 9:
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
          elif mob_at == 10:
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
          print('\nyou blocked the attack')
        else:
          print('\nyou failed your block\n')
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]*0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp

        
      elif attack == 'd':
        rand = random.randint(1,(Player.agility[0] + mob.agility[0]))
        if (rand + w) <= Player.agility[0]:
          print('you sucsessfuly dodged')
        else:
          print('\nyou failed to dodge\n')
          if mob_at >= 1 and mob_at <= 7:
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
          elif mob_at >= 8 and mob_at <= 9:
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
          elif mob_at == 10:
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp

          
      elif attack == 'run':
        rand = random.randint(1,(Player.agility[0] + mob.agility[0]))
        if (rand) <= Player.agility[0]:
          break
        else:
          print('\nyou failed to run\n')
          if mob_at >= 1 and mob_at <= 7:
            print(f"the {mob.name} is preparing to {mob.at[0]}")
            print('')
          elif mob_at >= 8 and mob_at <= 9:
            print(f"the {mob.name} is preparing to {mob.at_2[0]}")
            print('')
          elif mob_at == 10:
            print(f"the {mob.name} is preparing to {mob.s_at[0]}")
            print('')
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
      else:
          if mob_at >= 1 and mob_at <= 7:
            temp = int(round(mob.at[1]-(random.randint(w1,w2) * mob.at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at >= 8 and mob_at <= 9:
            temp = int(round(mob.at_2[1]-(random.randint(w1,w2) * mob.at_2[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
          elif mob_at == 10:
            temp = int(round(mob.s_at[1]-(random.randint(w1,w2) * mob.s_at[1]* 0.01)) * mob.strength[0])
            print('')
            print(f'you took {temp} damage')
            print('')
            Player.hp[0] -= temp
  if attack == 'run' and Player.hp[0] > 0:
    print(' ')
    print('you escaped')
    print(' ')
    Player.call_stats()
    print(' ')
    print(f'you killed the {mob.name}')
    Player.lvl[0] += int(mob.xp*lvl)
    print(' ')
    gp = random.randint(mob.gp[0],mob.gp[1])
    print(f'it droped {gp} gp and {int(mob.xp*lvl)} xp')
    Player.gp += gp
    print(' ')
    pick_loot(mob.l_t)
    print(' ')
    lvls()
  elif Player.hp[0] > 0:
    Player.call_stats()
    print(' ')
    print(f'you killed the {mob.name}')
    Player.lvl[0] += int(mob.xp*lvl)
    print(' ')
    gp = random.randint(mob.gp[0],mob.gp[1])
    print(f'it droped {gp} gp and {int(mob.xp*lvl)} xp')
    Player.gp += gp
    print(' ')
    pick_loot(mob.l_t)
    print(' ')
    lvls()
  else:
    print(' ')
    print(f'the {mob.name} killed you')
    print(' ')

def game_loop():
  while Player.hp[0] > 0:
    if Player.location == 1: ########################################################################################################################
      # random events
      pick_loot(common_forest)
      # player health check and stuff
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break

      # change location
      print("""you find yourself at the rivers edge next to an impassable cliff
      
      go with the cliff to your right [ r ]
      go with the river to your left [ l ]
      go into the forest [ f ] 
      """)
      main=input()
      if main == 'r':
        Player.location = 5
      elif main == 'l':
        Player.location = 2
      elif main == 'f':
        Player.location = one_two(5,6)
    elif Player.location == 2: ########################################################################################################################
      fight(f1)
      if Player.hp[0] <= 0:
        break
      pick_loot(common_forest)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself at the rivers edge
      
      go with the river to your right [ r ]
      go with the river to your left [ l ]
      go into the forest [ f ]
      """)
      main=input()
      if main == 'r':
        Player.location = 1
      elif main == 'l':
        Player.location = 3
      elif main == 'f':
        Player.location = one_two(6,7)
    elif Player.location == 3: ########################################################################################################################
      fight(f1)
      if Player.hp[0] <= 0:
        break
      pick_loot(common_forest)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself at the rivers edge
      
      go with the river to your right [ r ]
      go with the river to your left [ l ]
      go into the forest [ f ]
      """)
      main=input()
      if main == 'r':
        Player.location = 2
      elif main == 'l':
        Player.location = 4
      elif main == 'f':
        Player.location = one_two(7,8)
    elif Player.location == 4: ########################################################################################################################
      fight(f1)
      if Player.hp[0] <= 0:
        break
      pick_loot(common_forest)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself at the rivers edge
      
      go with the river to your right [ r ]
      go with the river to your left [ l ]
      go into the forest [ f ]
      """)
      main=input()
      if main == 'r':
        Player.location = 3
      elif main == 'l':
        Player.location = 9
      elif main == 'f':
        Player.location = 8
    elif Player.location == 5: ########################################################################################################################
      fight(f4)
      if Player.hp[0] <= 0:
        break
      pick_loot(rare_forest)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself next to an impassable cliff
      
      go with the cliff to your right [ r ]
      go with the cliff to your left [ l ]
      go into the forest [ f ] 
      """)
      main=input()
      if main == 'r':
        Player.location = 6
      elif main == 'l':
        Player.location = 1
      elif main == 'f':
        Player.location = one_two(1,6)
    elif Player.location == 6: ########################################################################################################################
      fight(f2)
      if Player.hp[0] <= 0:
        break
      pick_loot(common_forest)
      if random.randint(1,10) > 7:
        shop(shop_loot)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself next to an impassable cliff
      
      go with the cliff to your right [ r ]
      go with the cliff to your left [ l ]
      go into the forest [ f ] 
      """)
      main=input()
      if main == 'r':
        Player.location = 10
      elif main == 'l':
        Player.location = 5
      elif main == 'f':
        Player.location = one_two(2,7)
    elif Player.location == 7: ########################################################################################################################
      fight(f2)
      if Player.hp[0] <= 0:
        break
      pick_loot(common_forest)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself lost in the forest
      
      go right [ r ]
      go left [ l ]
      go backwards [ b ] 
      """)
      main=input()
      if main == 'r':
        Player.location = one_two(3,8)
      elif main == 'l':
        Player.location = one_two(2,6)
      elif main == 'b':
        Player.location = one_two(10,11)
    elif Player.location == 8: ########################################################################################################################
      fight(f4)
      if Player.hp[0] <= 0:
        break
      pick_loot(common_forest)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find youself at the abandoned shack
      
      go right [ r ]
      go left [ l ]
      go backwards [ b ] 
      go into the shack [ s ]
      """)
      main=input()
      if main == 'r':
        Player.location = one_two(4,9)
      elif main == 'l':
        Player.location = one_two(3,7)
      elif main == 'b':
        Player.location = one_two(11,12)
      elif main == 's':
        ins = True
        while ins:
          print("""you find yourself in the abandoned shack
      
          rest in the bed [ r ]
          cook food in the fireplace [ c ]
          store items in the chest [ s ] 
          leave the shack [ l ]
          """)
          main=input()
          if main == 'r':
            Player.agility[0] = Player.agility[1]
            Player.call_stats()
            print('')
            print('you wake up feeling well rested')
            print('')
          elif main == 'c':
            Player.cook()
          elif main == 's':
            Player.bank()
          elif main == 'l':
            ins = False
    elif Player.location == 9: ########################################################################################################################
      fight(f2)
      if Player.hp[0] <= 0:
        break
      pick_loot(common_forest)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself at the rivers edge
      
      go with the river to your right [ r ]
      go with the river to your left [ l ]
      go into the forest [ f ]
      """)
      main=input()
      if main == 'r':
        Player.location = 4
      elif main == 'l':
        Player.location = 13
      elif main == 'f':
        Player.location = one_two(8,12)
    elif Player.location == 10: ########################################################################################################################
      fight(f3)
      if Player.hp[0] <= 0:
        break
      pick_loot(uncommon_forest)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself next to an impassable cliff
      
      go with the cliff to your right [ r ]
      go with the cliff to your left [ l ]
      go into the forest [ f ] 
      """)
      main=input()
      if main == 'r':
        Player.location = 14
      elif main == 'l':
        Player.location = 6
      elif main == 'f':
        Player.location = one_two(11,7)
    elif Player.location == 11: ########################################################################################################################
      fight(f3)
      if Player.hp[0] <= 0:
        break
      pick_loot(uncommon_forest)
      if random.randint(1,10) > 7:
        shop(shop_loot)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself lost in the forest
      
      go right [ r ]
      go left [ l ]
      go backwards [ b ] 
      """)
      main=input()
      if main == 'r':
        Player.location = one_two(12,8)
      elif main == 'l':
        Player.location = one_two(10,7)
      elif main == 'b':
        Player.location = one_two(14,15)
    elif Player.location == 12: ########################################################################################################################
      fight(f3)
      if Player.hp[0] <= 0:
        break
      pick_loot(uncommon_forest)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself lost in the forest
      
      go right [ r ]
      go left [ l ]
      go backwards [ b ] 
      """)
      main=input()
      if main == 'r':
        Player.location = one_two(9,13)
      elif main == 'l':
        Player.location = one_two(8,11)
      elif main == 'b':
        Player.location = one_two(15,16)
    elif Player.location == 13: ########################################################################################################################
      fight(f3)
      if Player.hp[0] <= 0:
        break
      pick_loot(uncommon_forest)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself at the rivers edge
      
      go with the river to your right [ r ]
      go with the river to your left [ l ]
      go into the forest [ f ]
      """)
      main=input()
      if main == 'r':
        Player.location = 9
      elif main == 'l':
        Player.location = 16
      elif main == 'f':
        Player.location = 12
    elif Player.location == 14: ########################################################################################################################
      fight(f4)
      if Player.hp[0] <= 0:
        break
      pick_loot(rare_forest)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself next to an impassable cliff
      
      go with the cliff to your right [ r ]
      go with the cliff to your left [ l ]
      go into the forest [ f ] 
      """)
      main=input()
      if main == 'r':
        Player.location = 15
      elif main == 'l':
        Player.location = 10
      elif main == 'f':
        Player.location = 11
    elif Player.location == 15: ########################################################################################################################
      fight(de)
      if Player.hp[0] <= 0:
        break
      pick_loot(common_dungeon)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself next to an impassable cliff with a dungeon entrance
      
      go with the cliff to your right [ r ]
      go with the cliff to your left [ l ]
      go into the forest [ f ] 
      go into the dungeon [ d ]
      """)
      main=input()
      if main == 'r':
        Player.location = 16
      elif main == 'l':
        Player.location = 14
      elif main == 'f':
        Player.location = one_two(11,12)
      elif main == 'd':
        ind = True
        while ind:
          fight(d1)
          if Player.hp[0] <= 0:
            break
          print("""you find yourself in the catacombs
      
          go through bronze door to your right [ r ]
          go through black door to your right [ l ] 
          leave the dungeon [ d ]
          """)
          main = input()
          if main == 'r':
            while ind:
             fight(d2)
             if Player.hp[0] <= 0:
               break
             print("""you find yourself in the catacombs
      
             leave the dungeon [ d ]
             """)
             main = input()
             if main == 'd':
              pick_loot(common_dungeon)
              if Player.hp[0] <= 0:
                break
              Player.location = 15
              ind = False
          elif main == 'l':
            while ind:
              fight(d2)
              if Player.hp[0] <= 0:
                break
              print("""you find yourself in the catacombs
      
              go through red door to your right [ r ]
              go through dragon scale door to your right [ l ] 
              leave the dungeon [ d ]
              """)
              main = input()
              if main == 'r':
                while ind:
                  fight(d3)
                  if Player.hp[0] <= 0:
                    break
                  print("""you find yourself in the catacombs
      
                  leave the dungeon [ d ]
                  """)
                  main = input()
                  if main == 'd':
                    pick_loot(uncommon_dungeon)
                    if Player.hp[0] <= 0:
                      break
                    Player.location = 15
                    ind = False
              elif main == 'l':
                while ind:
                  fight(d4)
                  if Player.hp[0] <= 0:
                    break
                  print("""you find yourself in the dragons lair
      
                  leave the dungeon [ d ]
                  """)
                  main = input()
                  if main == 'd':
                    pick_loot(rare_dungeon)
                    if Player.hp[0] <= 0:
                      break
                    Player.location = 15
                    ind = False
              elif main == 'd':
                pick_loot(common_dungeon)
                if Player.hp[0] <= 0:
                  break
                Player.location = 15
                ind = False
          elif main == 'd':
            pick_loot(common_dungeon)
            if Player.hp[0] <= 0:
              break
            Player.location = 15
            ind = False
    elif Player.location == 16: ########################################################################################################################
      fight(f4)
      if Player.hp[0] <= 0:
        break
      pick_loot(rare_forest)
      if random.randint(1,10) > 7:
        shop(shop_loot)
      if Player.hp[0] <= 0:
        break
      player_stuff()
      if Player.hp[0] <= 0:
        break
      print("""you find yourself at the rivers edge next to an impassable cliff
      
      go with the river to your right [ r ]
      go with the cliff to your left [ l ]
      go into the forest [ f ] 
      """)
      main=input()
      if main == 'r':
        Player.location = 13
      elif main == 'l':
        Player.location = 15
      elif main == 'f':
        Player.location = 12
add_stats()
game_loop()
print('you died')
print('')
Player.check_inv()
Player.call_stats()
ind = input()
