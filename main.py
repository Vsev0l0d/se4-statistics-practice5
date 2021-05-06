from math import log
from prettytable import PrettyTable
import matplotlib.pyplot as plt

# Вариант 14
data = [-0.53, -0.87, -0.93, -0.41, 0.48, 0.81, -1.55, -1.42, -1.34, -0.61,
        -0.04, -0.33, -0.84, -1.33, 0.57, 0.62, 0.76, -0.48, 0.30, -0.35]

print("Исходный ряд:")
print(data)

print("Вариационный ряд:")
sorted_data = sorted(data)
print(sorted_data)

print("Первая и последняя порядковая статистика:", sorted_data[0], ";", sorted_data[-1])
print("Размах:", round(sorted_data[-1] - sorted_data[0], 2))

print("Статистический ряд:")
count_set = {}
for x in sorted_data:
    if count_set and x == list(count_set.keys())[-1]:
        count_set[x] += 1
    else:
        count_set[x] = 1

table = PrettyTable()
table.field_names = ["x(i)", *count_set.keys()]
table.add_row(["n(i)", *count_set.values()])
print(table)

avg = sum(data) / len(data)
print("Выборочное среднее:", avg)

dispersion = 0
for x in data:
    dispersion += (x - avg) ** 2
print("Дисперсия:", dispersion)
print("СКО:", dispersion ** 0.5)

print("Эмпирическая функция:")
plt.subplot(5, 1, 1)
plt.title("График эмпирической функции распределения")
n = len(count_set)
keys = list(count_set.keys())
y = 0
print(f'\t\t/ {round(y, 2)}, при x <= {keys[0]}')
for i in range(n - 1):
    y += count_set[keys[i]] / n if i < n else 0
    left = "F*(x) = " if i == n / 2 else "\t\t"
    print(f'{left}| {round(y, 2)}, при {keys[i]} < x <= {keys[i + 1]}')
    plt.plot([keys[i], keys[i + 1]], [y, y], c='black')
print(f'\t\t\\ {round(y, 2)}, при {keys[-1]} < x')


print("Интервальное статистическое распределение:")
h = round((sorted_data[-1] - sorted_data[0]) / (1 + round(log(n, 2))), 2)
curr_x = round(sorted_data[0] - h / 2, 2)
next_x = round(curr_x + h, 2)
grouped_data = {curr_x: 0}
for x in sorted_data:
    if x < next_x:
        grouped_data[curr_x] += 1 / n
    else:
        grouped_data[next_x] = 1 / n
        curr_x = next_x
        next_x = round(next_x + h, 2)
table = PrettyTable()
table.field_names = (f'[{round(x, 2)}; {round(x + h, 2)})' for x in grouped_data.keys())
table.add_row(list(round(x, 2) for x in grouped_data.values()))
print(table)

plt.subplot(5, 1, 3)
plt.title("Полигон частот")
plt.plot(list(grouped_data.keys()), list(grouped_data.values()), c='black')


plt.subplot(5, 1, 5)
plt.title("Гистограмма частот")
plt.bar(list(map(lambda x: x + h / 2, grouped_data.keys())), list(grouped_data.values()), width=h)
xticks = list(grouped_data.keys()) + [round(list(grouped_data.keys())[-1] + h, 2)]
plt.xticks(xticks, xticks)
plt.show()
