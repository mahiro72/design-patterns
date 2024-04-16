from threading import Thread, Lock
from typing import Any

class SingletonMeta(type):
    _instances  = {} # すべてのシングルトンのインスタンスを、メタクラスオブジェクトで管理する
    _lock: Lock = Lock()

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwds)
                cls._instances[cls] = instance

        # print(f"DEBUG: {cls._instances}")
        # 以下は実行結果の一部: 2つのシングルトンがcls._instancesに入っていることがわかる。
        # {<class '__main__.MySingleton'>: MySingleton(hoge), <class '__main__.MySingleton2'>: MySingleton2(hoge)}
        return cls._instances[cls]

class MySingleton(metaclass=SingletonMeta):
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"MySingleton({self.value})"

class MySingleton2(metaclass=SingletonMeta):
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"MySingleton2({self.value})"

def test_create_my_singletons(value: str, process_name: str):
    singleton = MySingleton(value=value)
    singleton2 = MySingleton2(value=value)
    print(f"{process_name}: singleton: {singleton}")
    print(f"{process_name}: singleton2: {singleton2}\n")

if __name__ == "__main__":
    """
    5-Singletonパターン

    インスタンスを1つしか存在しないように生成するパターン。
    """
    process1 = Thread(target=test_create_my_singletons, args=["hoge", "process1"])

    #　process2では新たに hoge2というvalueのインスタンスの作成を試みるが、
    # process1で既に作成したものが取得され、新規作成はされない。
    process2 = Thread(target=test_create_my_singletons, args=["hoge2", "process2"])

    process1.start()
    process2.start()
