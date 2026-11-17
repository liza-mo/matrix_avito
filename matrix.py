import aiohttp
import asyncio
import re
from typing import List


async def get_matrix(url: str) -> List[int]:
    print("Шаг 1: Начинаю скачивать данные...")

    text = ""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    text = await response.text()
                    print("Данные успешно скачаны!")
                else:
                    print("Сервер выдал ошибку. Код:", response.status)
                    return []
    except Exception as error:
        print("Ошибка сети! Не удалось скачать файл:", error)
        return []

    print("Шаг 2: Ищу все числа в тексте...")
    all_numbers_as_text = re.findall(r'\d+', text)

    numbers = []
    for num_text in all_numbers_as_text:
        numbers.append(int(num_text))

    print("Найдено чисел:", len(numbers))

    n = int(len(numbers) ** 0.5)
    print("Размер матрицы:", n, "на", n)

    print("Шаг 3: Собираю матрицу...")
    matrix = []
    count = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(numbers[count])
            count += 1
        matrix.append(row)

    print("Шаг 4: Иду по спирали...")
    result = []
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    while top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            result.append(matrix[i][left])
        left += 1

        for i in range(left, right + 1):
            result.append(matrix[bottom][i])
        bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][right])
            right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[top][i])
            top += 1

    print("Готово! Спираль собрана.")
    return result