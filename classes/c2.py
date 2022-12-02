class Animal:


    def __init__(self,name,age,color,region):
        self.name=name
        self.age=age
        self.color=color
        self.region=region
        self.is_domestic = False

    def info(self):
        print('animal details')
        print('name:',self.name)
        print('age:',self.age)
        print('color:',self.color)
        print('region:',self.region)

o1= Animal("elephant",10,'grey','africa')
o2=Animal("lion",5,'yellow','africa')

o1.info()
o2.info()