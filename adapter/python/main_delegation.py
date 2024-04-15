"""
委譲(Delegation) パターン
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

class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self._adaptee = adaptee

    def get_json(self) -> any:
        json_data = self.to_json_from_xml()
        return json_data

    def to_json_from_xml(self) -> any:
        # なんらかの変換処理
        return "json data"

if __name__ == "__main__":
    """
    もう一つのファイル(main_inheritance.py)の委譲バージョン。
    Adapterのインスタンス作成時にAdapteeをDIしている。
    """

    xml_getter = Adaptee(xml_data="xml data")
    json_getter = Adapter(adaptee=xml_getter)
    json_data = json_getter.get_json()
    print(f"data: {json_data}")
