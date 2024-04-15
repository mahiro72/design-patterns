from abc import ABC, abstractmethod

class AbstractDisplay(ABC):
    @abstractmethod
    def load_data(self) -> any: pass

    def display(self) -> None:
        data = self.load_data()
        print("data loaded")
        print(data)

class CSVDisplay(AbstractDisplay):
    def __init__(self, csv_path: str | None = None) -> None:
        self._csv_path = csv_path

    def load_data(self) -> any:
        # csv_pathからcsvを読み込む処理。今回はサンプル実装のため割愛
        return "csv data"

if __name__ == "__main__":
    """
    3-Template Methodパターン

    抽象クラスであるスーパークラス(AbstractDisplay) に、テンプレート機能と抽象メソッドがある。
    テンプレート機能内で、抽象メソッドが利用される。
    サブクラスでは、抽象メソッドの実装が行われ、今回の例ではcsvをロードするデータが実装されている。
    ExcelDisplayなど別データをロードするクラスにも機能拡張することができる。
    """

    csv_display = CSVDisplay(csv_path="./xxx/xxx.csv")
    csv_display.display()
