import copy

class Manager:
    def __init__(self) -> None:
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name):
        return copy.deepcopy(self._objects.get(name))

class Temp:
    def __deepcopy__(self, memo):
        print("hello")

class Product:
    def __init__(self, name) -> None:
        self.name = name
        self.t = Temp()

    def __copy__(self):
        new_product = Product(name=self.name)
        new_product.__dict__ = copy.copy(new_product.__dict__)
        return new_product

    def __deepcopy__(self, memo):
        print(memo)
        new_product = Product(name=self.name)
        memo[id(self)] = new_product
        print(memo)
        new_product.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new_product

if __name__ == "__main__":
    manager = Manager()

    p1 = Product(name="product1")
    p2 = Product(name="product2")
    manager.register_object("p1", p1)
    manager.register_object("p2", p2)

    p1_clone = manager.clone("p1")
    p2_clone = manager.clone("p2")



