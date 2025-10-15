import numpy as np
import matplotlib.pyplot as plt

def yakin_uyelik(mesafe):
    if mesafe < 200:
        return 1
    elif 200 <= mesafe <= 500:
        return (500 - mesafe) / 300
    else:
        return 0

def graph_ciz(x_values, target = None):
    y_values = []
    target_y = -1
    for i in x_values:
        y_values.append(yakin_uyelik(i))
    plt.figure(figsize=(12, 7))
    plt.plot(x_values, y_values, 'b-', linewidth=2, label='Bulanık Kümesi')
    plt.title('Üyelik Fonksiyonu', fontsize=14, fontweight='bold')
    plt.xlabel('u Degeri', fontsize=12, fontweight='bold')
    plt.ylabel('Üyelik Derecesi', fontsize=12, fontweight='bold')  
    plt.xlim(-600, 600)
    plt.ylim(0, 1.1)
    
    plt.grid()
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3, linewidth=2)
    if target is None:
        plt.plot([200, 200], [0, 1], 'r--', alpha=0.7, linewidth=1)
        plt.axhline(y=1, color='k', linestyle=':', alpha=0.5)
        plt.axhline(y=0, color='k', linestyle=':', alpha=0.5)   
    else:
        target_y = yakin_uyelik(target)
        plt.plot([target, target], [0, target_y], 'r--', alpha=0.7, linewidth=1)
        plt.plot([x_values[0], target], [target_y, target_y], 'g--', alpha=0.7, linewidth=1)
        plt.xticks(list(plt.xticks()[0]) + [target]) 
        plt.yticks(list(plt.yticks()[0]) + [target_y]) 
        plt.plot(target, target_y, 'ro', markersize=5, label=f'u={target}, μ={target_y}')
    plt.legend()
    plt.show()
    return target_y

try: 
    target =  int(input("Deger giriniz ya da bos birakiniz : "))
except ValueError:
   target = None

mesafe_degerleri = np.linspace(-600, 600, 1000)
result = graph_ciz(x_values=mesafe_degerleri, target= target)

if result != -1:
    print(result)

