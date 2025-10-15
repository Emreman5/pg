import numpy as np
import matplotlib.pyplot as plt

def mu_A(x):
    return 1 / (1 + 10 * (x - 5)**2)

def graph_ciz(x_values, target=None):
    y_values = mu_A(x_values)
    
    plt.figure(figsize=(12, 7))
    plt.plot(x_values, y_values, 'b-', linewidth=2)
    plt.xlabel('x degerleri', fontsize=12, fontweight='bold')
    plt.ylabel('Uyelik derecesi', fontsize=12, fontweight='bold')
    plt.title('Üyelik Fonksiyonu', fontsize=14, fontweight='bold')
    plt.grid()
    plt.ylim(0, 1)
    plt.xlim(0, 10)
    
    if target is None:
        plt.axvline(x=5, color='r', linestyle='--', alpha=0.7, linewidth=1)
        plt.xticks(list(plt.xticks()[0]) + [5])
        result = -1
    else:
        target_y = mu_A(target)
        plt.plot([target, target], [0, target_y], 'r--', alpha=0.7, linewidth=1)
        plt.plot([x_values[0], target], [target_y, target_y], 'g--', alpha=0.7, linewidth=1)
        plt.xticks(list(plt.xticks()[0]) + [target])
        plt.yticks(list(plt.yticks()[0]) + [target_y])
        plt.plot(target, target_y, 'ro', markersize=5, label=f'u={target}, μ={target_y}')
        result = target_y
    
    plt.show()
    return result

x_values = np.linspace(0, 10, 1000)

try: 
    target = int(input("Deger giriniz ya da bos birakiniz: ") or "0") or None
except ValueError:
    target = None

result = graph_ciz(x_values=x_values, target=target)

if result != -1:
    print(result)