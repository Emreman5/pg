import numpy as np
import matplotlib.pyplot as plt

sicaklik = np.arange(20, 81, 1)

def low_uyelik(x):
    if x <= 20: return 0.0
    elif 20 < x <= 25: return (x - 20) / 5
    elif 25 < x <= 35: return 1.0
    elif 35 < x <= 40: return (40 - x) / 5
    else: return 0.0

def medium_uyelik(x):
    if x <= 30: return 0.0
    elif 30 < x <= 42: return (x - 30) / 12
    elif 42 < x <= 55: return 1.0
    elif 55 < x <= 80: return (80 - x) / 25
    else: return 0.0

low_values = [low_uyelik(x) for x in sicaklik]
medium_values = [medium_uyelik(x) for x in sicaklik]

kural1_oncesil = 0.4
kural2_oncesil = 0.75

kural1_mamdani = [min(kural1_oncesil, u) for u in low_values]
kural2_mamdani = [min(kural2_oncesil, u) for u in medium_values]
kural1_larsen = [kural1_oncesil * u for u in low_values]
kural2_larsen = [kural2_oncesil * u for u in medium_values]

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

axes[0,0].plot(sicaklik, low_values, 'b-', linewidth=2, label='Low', alpha=0.7)
axes[0,0].plot(sicaklik, kural1_mamdani, 'r-', linewidth=3, label='Mamdani')
axes[0,0].axhline(y=kural1_oncesil, color='g', linestyle='--', alpha=0.7)
axes[0,0].set_title('Kural 1: Low → Mamdani')
axes[0,0].set_xlabel('Sıcaklık (°C)')
axes[0,0].set_ylabel('Üyelik')
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)

axes[0,1].plot(sicaklik, medium_values, 'g-', linewidth=2, label='Medium', alpha=0.7)
axes[0,1].plot(sicaklik, kural2_mamdani, 'r-', linewidth=3, label='Mamdani')
axes[0,1].axhline(y=kural2_oncesil, color='b', linestyle='--', alpha=0.7)
axes[0,1].set_title('Kural 2: Medium → Mamdani')
axes[0,1].set_xlabel('Sıcaklık (°C)')
axes[0,1].set_ylabel('Üyelik')
axes[0,1].legend()
axes[0,1].grid(True, alpha=0.3)

axes[1,0].plot(sicaklik, low_values, 'b-', linewidth=2, label='Low', alpha=0.7)
axes[1,0].plot(sicaklik, kural1_larsen, 'r-', linewidth=3, label='Larsen')
axes[1,0].axhline(y=kural1_oncesil, color='g', linestyle='--', alpha=0.7)
axes[1,0].set_title('Kural 1: Low → Larsen')
axes[1,0].set_xlabel('Sıcaklık (°C)')
axes[1,0].set_ylabel('Üyelik')
axes[1,0].legend()
axes[1,0].grid(True, alpha=0.3)

axes[1,1].plot(sicaklik, medium_values, 'g-', linewidth=2, label='Medium', alpha=0.7)
axes[1,1].plot(sicaklik, kural2_larsen, 'r-', linewidth=3, label='Larsen')
axes[1,1].axhline(y=kural2_oncesil, color='b', linestyle='--', alpha=0.7)
axes[1,1].set_title('Kural 2: Medium → Larsen')
axes[1,1].set_xlabel('Sıcaklık (°C)')
axes[1,1].set_ylabel('Üyelik')
axes[1,1].legend()
axes[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

birlesik_mamdani = [max(kural1_mamdani[i], kural2_mamdani[i]) for i in range(len(sicaklik))]
birlesik_larsen = [max(kural1_larsen[i], kural2_larsen[i]) for i in range(len(sicaklik))]

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(sicaklik, kural1_mamdani, 'b--', linewidth=2, label='Kural 1', alpha=0.7)
plt.plot(sicaklik, kural2_mamdani, 'g--', linewidth=2, label='Kural 2', alpha=0.7)
plt.plot(sicaklik, birlesik_mamdani, 'r-', linewidth=3, label='Birleşik')
plt.title('Birleşik Mamdani Çıkarım')
plt.xlabel('Sıcaklık (°C)')
plt.ylabel('Üyelik')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 1, 2)
plt.plot(sicaklik, kural1_larsen, 'b--', linewidth=2, label='Kural 1', alpha=0.7)
plt.plot(sicaklik, kural2_larsen, 'g--', linewidth=2, label='Kural 2', alpha=0.7)
plt.plot(sicaklik, birlesik_larsen, 'r-', linewidth=3, label='Birleşik')
plt.title('Birleşik Larsen Çıkarım')
plt.xlabel('Sıcaklık (°C)')
plt.ylabel('Üyelik')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()