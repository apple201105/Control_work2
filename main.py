
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