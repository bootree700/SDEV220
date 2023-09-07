class Mario():

    def move(self):
        print('I am moving!')

class Shroom():

    def eat_shroom(self):
        print("Now I am big!")

class BigMario(Mario, Shroom):
    pass #needs a line, but don't want it to do anything

bm = BigMario()

bm.move()
bm.eat_shroom()