import numpy as np
import matplotlib.pyplot as plt

def kuvvet(u, n=2):
    return u ** n

def derisim(u):
    return u ** 2

def genislemem(u):
    return np.sqrt(u)

def yogunlasma(u):
    if u <= 0.5: return 2 * u**2
    else: return 1 - 2 * (1 - u)**2

def islem_uygula(x, arr, islem_func, isim, func_name, ux_degeri=None, uy_degeri = None):
    islemli = [islem_func(u) for u in arr]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, arr, 'b-', linewidth=2, label= "orijinal")
    plt.plot(x, islemli, 'r-', linewidth=2, label=isim)
    
    if uy_degeri:  
        u_islem = islem_func(uy_degeri)
        plt.axvline(x=ux_degeri, color='green', linestyle='--', alpha=0.7)
        plt.plot(ux_degeri, uy_degeri, 'bo', markersize=8, label=f'Orijinal: {uy_degeri:.3f}')
        plt.plot(ux_degeri, u_islem, 'ro', markersize=8, label=f'{isim}: {u_islem:.3f}')
        print(f"{isim}: u={ux_degeri}, μ={u_islem:.3f}")
    
    plt.title(f'{func_name} - {isim} İşlemi',fontweight='bold', fontsize=14)
    plt.xlabel('x',fontweight='bold', fontsize=12)
    plt.ylabel('Uyelik Derecesi',fontweight='bold', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 1.1)
    plt.show()
