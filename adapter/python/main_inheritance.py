"""
継承(Inheritance) パターン
"""
from abc import ABC, abstractmethod

class Target(ABC):
    @abstractmethod
    def get_json(self) -> any: pass

class Adaptee:
    def __init__(self, xml_data: str | None = None) -> None:
        self._xml_data = xml_data

    def get_xml(self) -> any:
        return self._xml_data

class Adapter(Target, Adaptee):
    def __init__(self, xml_data: str | None = None) -> None:
        self._xml_data = xml_data

    def get_json(self) -> any:
        json_data = self.to_json_from_xml()
        return json_data

    def to_json_from_xml(self) -> any:
        # なんらかの変換処理
        return "json data"

if __name__ == "__main__":
    """
    2-Adapterパターン

    これまではTargetインターフェース満たす別のオブジェクトを利用してjsonデータを取得していた。
    今回の例では、Targetインターフェースと他のクラス(Adaptee)を継承した、新しいクラス(Adapter)を用意することで、
    xmlデータからjsonデータを取得できるようになり、既存のコードと置き換えができる。
    元のインターフェースと他のクラスの両方を継承した、新しいクラスをラッパーとして活用するパターンをAdapterパターンという。
    """

    json_getter = Adapter(xml_data="xml data")
    json_data = json_getter.get_json()
    print(f"data: {json_data}")
