class Cat:
    name= ""
    age=0
    furcolor=""
    breed=""

    def eat(self):
        print( "cat is eating 🐠")
    
    def sleep(self):
        print("cat is sleeping!")

#creating objects
tom = Cat()
snow = Cat()

#updating attributes
tom.name="Tom"
tom.age=3
tom.fur_color='gray'
tom.breed='city cat'
snow.name='snowbell'
snow.age=5
snow.fur_color='white'
snow.breed='persian'

#calling methods
tom.eat()
snow.sleep()
tom.sleep()

#displaying attributes
print(tom.name,tom.age,tom.fur_color,tom.breed)
print(snow.name,snow.age,snow.fur_color,snow.breed)
