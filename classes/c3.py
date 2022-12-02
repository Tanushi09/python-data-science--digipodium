import random
#class subclass(super_class
class MyList(list):#inherited lists
    
    def shuffle(self):
        random.shuffle(self)
    
    def get_random(self):
        return random.choice(self)


#object

a=MyList([12,121,3])
a.sort()
print(a)
a.shuffle()
print(a)
print('random item from list=',a.get_random())