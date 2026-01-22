from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки подсчетами
    if not container:  # Если массив пустой, возвращаем его как есть
        return container
    

    max_val = max(container)
    min_val = min(container)
    
   
    count_size = max_val - min_val + 1
    count = [0] * count_size
    
   
    for num in container:
        count[num - min_val] += 1
    
   
    result = []
    for i in range(count_size):
        result.extend([i + min_val] * count[i])
    
    return result
