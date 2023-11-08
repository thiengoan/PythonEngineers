class Car:
    sound = 'beep'
    #color = 'red'

    def __init__(seft,color):
        seft.color = 'blue'

    def sayHello(seft):
        print('Hello')  

    def Tall():
        print('Alo Alo')   

bmw = Car('red')
toyota = Car('blue')


bmw.color = 'Black'
toyota.sound = 'Ụn Ụn'

print(bmw.sound)
print(toyota.sound)
print(bmw.color)
print(toyota.color)
bmw.sayHello()

Car.Tall()