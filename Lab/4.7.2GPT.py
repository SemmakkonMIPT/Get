import numpy as np
import matplotlib.pyplot as plt

# Управление выводом графиков
N = [1]  # Укажите в этом списке номера графиков, которые нужно построить

# Исходные данные
L = 96.5  # см
lambda_laser = 0.63e-4  # см
radiuses_cm = np.array([1.0, 0.4, 0.3, 0.25, 0.3, 0.25, 0.2, 0.2, 0.2, 0.2])  # радиусы в см
radiuses_cm = radiuses_cm[1:][::-1]  # Убираем первую точку, затем инвертируем порядок
m_values = np.arange(1, len(radiuses_cm) + 1)  # номера колец
r_squared = radiuses_cm ** 2

# Линейная регрессия
slope, intercept = np.polyfit(m_values, r_squared, 1)
no_minus_ne = lambda_laser / L / slope  # Вычисление no-ne

# Расчет полуволнового напряжения
v_per_div = 1.5  # в киловольтах
U_half_wave = 98 * v_per_div / 100  # полуволновое напряжение

# Вывод результатов расчетов
print(f"Полученное значение (no - ne): {no_minus_ne}")
print(f"Полученное полуволновое напряжение: {U_half_wave} кВ")

# Построение графика
if 1 in N:
    plt.figure(figsize=(8, 6))
    plt.plot(m_values, r_squared, 'o-', label='Экспериментальные данные')
    plt.xlabel('Номер тёмного кольца m')
    plt.ylabel('Квадрат радиуса, см²')
    plt.title('Зависимость квадрата радиуса тёмного кольца от его номера (без первой точки)')
    plt.grid(True)

    # Линия тренда
    trendline = intercept + slope * m_values
    plt.plot(m_values, trendline, 'r--', label=f'Линия тренда (наклон: {slope:.5f})')

    plt.legend()
    plt.show()
