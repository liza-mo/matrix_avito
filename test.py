import asyncio
from matrix import get_matrix

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]

def test_get_matrix():
    result = asyncio.run(get_matrix(SOURCE_URL))
    assert result == TRAVERSAL, f"Ошибка! Ожидалось {TRAVERSAL}, а получилось {result}"
    print("Тест пройден")

if __name__ == "__main__":
    test_get_matrix()