from collections.abc import Iterator, Iterable

class BookShelf(Iterable):
    """
    BookShelfは、Iteratorを生成するIterableの実装です。配列の実態の管理はここで行います。
    """
    def __init__(self, collection: list[str] = []) -> None:
        self._collection = collection

    def __iter__(self) -> Iterator:
        return BookShelfIterator(self)

    def __repr__(self) -> str:
        return f"BookShelf({self._collection})"

    def get_collection(self) -> list[str]:
        return self._collection

    def append(self, book: str):
        self._collection.append(book)


class BookShelfIterator(Iterator):
    """
    1-Iteratorパターン

    BookShelfIteratorは、順番に要素にアクセスするIteratorの実装。
    各Iteratorごとにindexを持っており、1つのIterableから複数のIteratorを生成できる。
    """
    def __init__(self, book_shelf: BookShelf) -> None:
       self._collection = book_shelf.get_collection()
       self.index = 0

    def __next__(self) -> str:
        if self.index < len(self._collection):
            value = self._collection[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration()

if __name__ == "__main__":
    book_shelf = BookShelf()
    book_shelf.append("bookA")
    book_shelf.append("bookB")
    book_shelf.append("bookC")

    print(book_shelf)
    print("\n".join(book_shelf))
