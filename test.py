class A:
    @property
    def name(self):
        return self.__class__.__name__.replace("State", "")


a = A()

print(a.name)