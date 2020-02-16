class Singleton(type):
    def __init__(self,*args, **kwargs):
        print('in __init')
        self.__instane = None
        super(Singleton,self).__init__(*args, **kwargs)
    def __call__(self, *args, **kwargs):
        print('in __call')
        if self.__instane is None:
            self.__instane = super(Singleton,self).__call__(*args, **kwargs)
            print(type(self.__instane))
        return self.__instane

class Myclass(metaclass=Singleton):
    pass

my1 = Myclass()
my2 = Myclass()
print(my1 == my2)
