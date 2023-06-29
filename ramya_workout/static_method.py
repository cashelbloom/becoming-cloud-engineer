class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi()


class Bar:
    @staticmethod
    def hi():
        print('Hello, I do not take parameters')


another_object = Bar()
another_object.hi()
