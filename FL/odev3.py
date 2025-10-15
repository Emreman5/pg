import numpy as np
import matplotlib.pyplot as plt
import utils as util

def uyelik_hesapla(a, b, c, d, u, tip):
    if tip == 'sol_omuz':
        if u <= a: return 0
        if u <= b: return 2 * ((u - a) / (c - a))**2
        if u <= c: return 1 - 2 * ((u - c) / (c - a))**2
        return 0
    elif tip == 'sag_omuz':
        if u <= a: return 0
        if u <= b: return 1 - 2 * ((u - a) / (c - a))**2
        if u <= c: return 2 * ((u - c) / (c - a))**2
        return 0
    elif tip == 'ucgen':
        if u <= a: return 0
        if u <= b: return (u - a) / (b - a)
        if u <= c: return (c - u) / (c - b)
        return 0
    elif tip == 'yamuk':
        if u <= a: return 0
        if u <= b: return (u - a) / (b - a)
        if u <= c: return 1
        if u <= d: return (d - u) / (d - c)
        return 0

def omuz_uyelik_hesapla(x, b_genislik, c_orta):
    a_sol = c_orta - b_genislik
    b_sol = c_orta - b_genislik / 2
    c_sol = c_orta
    a_sag = c_orta
    b_sag = c_orta + b_genislik / 2
    c_sag = c_orta + b_genislik
    
    z = []
    for u in x:
        sol_deger = uyelik_hesapla(a_sol, b_sol, c_sol, None, u, 'sol_omuz')
        sag_deger = uyelik_hesapla(a_sag, b_sag, c_sag, None, u, 'sag_omuz')
        z.append(max(sol_deger, sag_deger))
    return z

def u_degeri_uyelik_hesapla(tip, params, u_degeri):
    if tip == 'omuz':
        b_genislik, c_orta = params
        a_sol = c_orta - b_genislik
        b_sol = c_orta - b_genislik / 2
        c_sol = c_orta
        a_sag = c_orta
        b_sag = c_orta + b_genislik / 2
        c_sag = c_orta + b_genislik
        
        sol_deger = uyelik_hesapla(a_sol, b_sol, c_sol, None, u_degeri, 'sol_omuz')
        sag_deger = uyelik_hesapla(a_sag, b_sag, c_sag, None, u_degeri, 'sag_omuz')
        return max(sol_deger, sag_deger)
        
    elif tip == 'ucgen':
        a, b, c = params
        return uyelik_hesapla(a, b, c, None, u_degeri, 'ucgen')
        
    elif tip == 'yamuk':
        a, b, c, d = params
        return uyelik_hesapla(a, b, c, d, u_degeri, 'yamuk')

def fonksiyon_ciz(x, tip, params, u_degeri=None, renk='purple', isim='Fonksiyon', returnUyelik=False):
    if tip == 'omuz':
        z = omuz_uyelik_hesapla(x, *params)
    elif tip == 'ucgen':
        a, b, c = params
        z = [uyelik_hesapla(a, b, c, None, u, 'ucgen') for u in x]
    elif tip == 'yamuk':
        a, b, c, d = params
        z = [uyelik_hesapla(a, b, c, d, u, 'yamuk') for u in x]
    
    if returnUyelik:
        uyelik = u_degeri_uyelik_hesapla(tip, params, u_degeri) if u_degeri else 0
        return z, uyelik
    
    plt.figure(figsize=(12, 6))
    plt.plot(x, z, color=renk, linewidth=2, label=isim)
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    
    if u_degeri:
        uyelik = u_degeri_uyelik_hesapla(tip, params, u_degeri)
        
        plt.axvline(x=u_degeri, color='red', linestyle='--', alpha=0.7)
        plt.plot([x[0], u_degeri], [uyelik, uyelik], 'g--', alpha=0.7, linewidth=1)
        plt.xticks(list(plt.xticks()[0]) + [u_degeri]) 
        plt.yticks(list(plt.yticks()[0]) + [uyelik]) 
        plt.plot(u_degeri, uyelik, 'o', color=renk, markersize=8, 
                label=f'u={u_degeri}, μ={uyelik:.3f}')       
        print(f"{isim}: u={u_degeri}, μ={uyelik:.3f}")

    plt.title(f'{isim} Üyelik Fonksiyonu')
    plt.xlabel('u Değeri')
    plt.ylabel('Üyelik Derecesi')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 1.1)
    plt.show()

def bulanik_Islem(x, params, islem_func, isim,func_name, u=None, tip = "omuz"):
    z, uyelik = fonksiyon_ciz(x, tip, params, u, 'purple', isim, returnUyelik=True)
    
    if u:
        util.islem_uygula(x, z, islem_func, isim, func_name,uy_degeri= uyelik, ux_degeri= u)
    else:
         util.islem_uygula(x, z, islem_func, isim, func_name)
         
if __name__ == "__main__":
    x = np.arange(0, 101)
    omuz_genislik = 40
    omuz_orta_nokta = 50
    
    try:
        u_degeri = int(input("u değeri girin (0-100, boş=bırak): ") or "0") or None
    except: 
        u_degeri = None
        
bulanik_Islem(x,(30,40,50,60), util.yogunlasma, 'yogunlasma', 'birlesik omuz', u_degeri, tip= "yamuk")