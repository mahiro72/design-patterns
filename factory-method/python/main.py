from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def use(self) -> None: pass

class Factory(ABC):
    def create(self, owner: str) -> Product:
        product = self.create_product(owner=owner)
        self.register_product(product)
        return product

    @abstractmethod
    def create_product(self, owner: str) -> Product: pass

    @abstractmethod
    def register_product(self, product: Product) -> None: pass

class IDCard(Product):
    def __init__(self, owner: str) -> None:
        self._owner = owner

    def __repr__(self) -> str:
        return f"IDCard({self._owner})"

    def use(self) -> None:
        print(f"use {self}")

class IDCardFactory(Factory):
    def create_product(self, owner: str) -> Product:
        return IDCard(owner=owner)

    def register_product(self, product: Product) -> None:
        # DBに登録するなどの永続処理をする。ここでは割愛
        pass

if __name__ == "__main__":
    """
    4-Factory Methodパターン

    抽象クラスのFactoryとProductの抽象メソッドを用いることで、クライアントで具体的なオブジェクトの生成ロジックを隠蔽する。
    また関連する製品群(MemberCardなど)でも、今回作成したFactoryやProductを再利用することができる。
    関連しない概念(例えばユーザ情報を扱うMemberなど)では、再利用できない部分は新しいFactoryやProductなどの抽象クラスから新たに設計する必要がある。
    """
    id_card_factory = IDCardFactory()

    id_card1 = id_card_factory.create("taro")
    id_card2 = id_card_factory.create("hanako")

    id_card1.use()
    id_card2.use()
