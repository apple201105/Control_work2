Тимошенко Родио МФ 72 вариант B
1
import pandas as pd


file_path = input('введите название файла Excel')

df = pd.read_excel(file_path)

print(f"Всего строк в таблице: {len(df)}")

row_number = int(input("Введите номер строки: "))


if 0 <= row_number < len(df):
    print("\nСтрока", row_number)
    print(df.iloc[row_number])
else:
    print("Ошибка: такой строки нет")

2
import pandas as pd
import matplotlib.pyplot as plt


file_path = 'Книга1.xlsx'
df = pd.read_excel(file_path)
plt.figure(figsize=(8, 6))
plt.plot(df['x'], df['y'], marker='o', label='Зависимость y от x')
plt.title('График из Excel')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.legend()
plt.grid(True)  
plt.show()

3.
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


x = np.linspace(3, 5, 100)
y = np.linspace(-5, 4, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**3 + y**2))


ax.plot_surface(x, y, z, cmap='viridis')


ax.set_title("Простая 3D поверхность")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
