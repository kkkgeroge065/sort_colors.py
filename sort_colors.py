def brightness(color):
    """Вычисляет яркость цвета"""
    return sum(color) / 3

def sort_colors(colors):
    """Сортирует цвета по яркости"""
    return sorted(colors, key=brightness)

# Пример использования
colors = [
    [255, 0, 0], # красный
    [0, 255, 0], # зеленый
    [0, 0, 255], # синий
    [255, 255, 0], # желтый
    [255, 255, 255], # белый
    [0, 0, 0] # черный
]
sorted_colors = sort_colors(colors)
print(sorted_colors) # [[0, 0, 0], [0, 0, 255], [0, 255, 0], [255, 0, 0], [255, 255, 0], [255, 255, 255]]
