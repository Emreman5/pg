import numpy as np
import matplotlib.pyplot as plt

# Evrensel küme
sicaklik = np.arange(20, 81, 1)

# Low bulanık kümesi (yamuk) - a=20, b=25, c=35, d=40
def low_uyelik(x):
    if x <= 20:
        return 0.0
    elif 20 < x <= 25:
        return (x - 20) / (25 - 20)
    elif 25 < x <= 35:
        return 1.0
    elif 35 < x <= 40:
        return (40 - x) / (40 - 35)
    else:
        return 0.0

# Medium bulanık kümesi (yamuk) - a=30, b=42, c=55, d=80
def medium_uyelik(x):
    if x <= 30:
        return 0.0
    elif 30 < x <= 42:
        return (x - 30) / (42 - 30)
    elif 42 < x <= 55:
        return 1.0
    elif 55 < x <= 80:
        return (80 - x) / (80 - 55)
    else:
        return 0.0

# Üyelik değerlerini hesapla
low_values = [low_uyelik(x) for x in sicaklik]
medium_values = [medium_uyelik(x) for x in sicaklik]

# Grafik çiz
plt.figure(figsize=(12, 6))

# Low kümesi
plt.plot(sicaklik, low_values, 'b-', linewidth=3, label='Low Sıcaklık')

# Medium kümesi
plt.plot(sicaklik, medium_values, 'g-', linewidth=3, label='Medium Sıcaklık')

# Low kümesi için kritik noktaları işaretle
low_points_x = [20, 25, 35, 40]
low_points_y = [low_uyelik(x) for x in low_points_x]
plt.plot(low_points_x, low_points_y, 'bo', markersize=8)

# Medium kümesi için kritik noktaları işaretle
med_points_x = [30, 42, 55, 80]
med_points_y = [medium_uyelik(x) for x in med_points_x]
plt.plot(med_points_x, med_points_y, 'go', markersize=8)

# Noktaları etiketle
for x, y in zip(low_points_x, low_points_y):
    plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

for x, y in zip(med_points_x, med_points_y):
    plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

plt.title('Low ve Medium Bulanık Kümeleri', fontsize=14, fontweight='bold')
plt.xlabel('Sıcaklık (°C)', fontsize=12)
plt.ylabel('Üyelik Derecesi', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.ylim(0, 1.1)
plt.xlim(0, 80)
plt.xticks([20, 25, 30, 35, 40, 42, 50, 55, 60, 70, 80])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

plt.tight_layout()
plt.show()

# Küme parametrelerini yazdır
print("LOW KÜMESİ (Yamuk):")
print(f"a=20, b=25, c=35, d=40")
print(f"20-25°C: 0'dan 1'e artan")
print(f"25-35°C: 1 (çekirdek)")
print(f"35-40°C: 1'den 0'a azalan")
print(f"<20 ve >40: 0")

print("\nMEDIUM KÜMESİ (Yamuk):")
print(f"a=30, b=42, c=55, d=80")
print(f"30-42°C: 0'dan 1'e artan")
print(f"42-55°C: 1 (çekirdek)")
print(f"55-80°C: 1'den 0'a azalan")
print(f"<30 ve >80: 0")