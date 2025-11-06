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

def tnorm_min(u1, u2): return min(u1, u2)
def tnorm_algebric_product(u1, u2): return u1 * u2
def tnorm_bounded_product(u1, u2): return max(0, u1 + u2 - 1)
def tnorm_drastic_product(u1, u2):
    if u1 == 1: return u2
    elif u2 == 1: return u1
    else: return 0

def snorm_max(u1, u2): return max(u1, u2)
def snorm_algebric_sum(u1, u2): return u1 + u2 - u1 * u2
def snorm_bounded_sum(u1, u2): return min(1, u1 + u2)
def snorm_drastic_sum(u1, u2):
    if u1 == 0: return u2
    elif u2 == 0: return u1
    else: return 1

def orijinal_kumeleri_goster():
    plt.figure(figsize=(12, 6))
    plt.plot(sicaklik, low_values, 'b-', linewidth=3, label='Low')
    plt.plot(sicaklik, medium_values, 'g-', linewidth=3, label='Medium')
    low_points_x = [20, 25, 35, 40]
    low_points_y = [low_uyelik(x) for x in low_points_x]
    plt.plot(low_points_x, low_points_y, 'bo', markersize=8)
    med_points_x = [30, 42, 55, 80]
    med_points_y = [medium_uyelik(x) for x in med_points_x]
    plt.plot(med_points_x, med_points_y, 'go', markersize=8)
    plt.title('Low ve Medium Bulanık Kümeleri')
    plt.xlabel('Sıcaklık (°C)')
    plt.ylabel('Üyelik Derecesi')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 1.1)
    plt.xlim(20, 80)
    plt.xticks([20, 30, 40, 50, 60, 70, 80])
    plt.show()

def tum_operatorleri_uygula():
    tnorm_operators = [
        ('Min T-norm', tnorm_min),
        ('Cebirsel Çarpım', tnorm_algebric_product),
        ('Sınırlı Çarpım', tnorm_bounded_product),
        ('Güçlü Çarpım', tnorm_drastic_product)
    ]
    
    snorm_operators = [
        ('Max S-norm', snorm_max),
        ('Cebirsel Toplam', snorm_algebric_sum),
        ('Sınırlı Toplam', snorm_bounded_sum),
        ('Güçlü Toplam', snorm_drastic_sum)
    ]
    
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    fig.suptitle('Tüm T-norm ve S-norm Operatörleri')
    
    for i, (name, tnorm_func) in enumerate(tnorm_operators):
        kesisim = [tnorm_func(low_values[j], medium_values[j]) for j in range(len(sicaklik))]
        ax = axes[0, i]
        ax.plot(sicaklik, low_values, 'b-', linewidth=2, label='Low', alpha=0.7)
        ax.plot(sicaklik, medium_values, 'g-', linewidth=2, label='Medium', alpha=0.7)
        ax.plot(sicaklik, kesisim, 'r-', linewidth=3, label='Kesişim')
        ax.set_title(name)
        ax.set_xlabel('Sıcaklık (°C)')
        ax.set_ylabel('Üyelik Derecesi')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.1)
        ax.set_xlim(20, 80)
    
    for i, (name, snorm_func) in enumerate(snorm_operators):
        birlesim = [snorm_func(low_values[j], medium_values[j]) for j in range(len(sicaklik))]
        ax = axes[1, i]
        ax.plot(sicaklik, low_values, 'b-', linewidth=2, label='Low', alpha=0.7)
        ax.plot(sicaklik, medium_values, 'g-', linewidth=2, label='Medium', alpha=0.7)
        ax.plot(sicaklik, birlesim, 'r-', linewidth=3, label='Birleşim')
        ax.set_title(name)
        ax.set_xlabel('Sıcaklık (°C)')
        ax.set_ylabel('Üyelik Derecesi')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.1)
        ax.set_xlim(20, 80)
    
    plt.tight_layout()
    plt.show()
    

if __name__ == "__main__":
    orijinal_kumeleri_goster()
    tum_operatorleri_uygula()