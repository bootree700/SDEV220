#create a class called Enemy.
#we do not have any class variables

class Enemy:
    def __init__(self,energy):
        self.energy = energy
    
    #other methods/functions besides init
    def get_energy(self):
        print(self.energy) #self essentially is the instance name and is used in place of it

jason = Enemy(5)
jason.get_energy()

sally = Enemy(6)
sally.get_energy()