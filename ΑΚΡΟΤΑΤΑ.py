def megisto(sinartisi):
    from sympy import Symbol,Function, diff, sin, exp, solve, lambdify
    import numpy as np
    import matplotlib.pyplot as plt
    x = Symbol('x')
    i = Symbol('i')
    f = Symbol('f')
    sinar = Symbol('sinar')
    first = diff(sinartisi, x)
    second = diff(first, x)
    lisi = solve(first,x)
    f = lambdify(x,second)
    sinar = lambdify(x,sinartisi)
    
    for k in lisi:
        if k<6:
            x_vals = np.linspace(-7, 7,100)
        elif k >6 and k<10:
            x_vals = np.linspace(-10, 10,100) 
        elif k >10 and k <20:
            x_vals = np.linspace(-50, 50,100)
        else:
            x_vals = np.linspace(-70, 70,100)
    y_vals = np.array([sinar(x) for x in x_vals])
    fig, ax=plt.subplots(figsize=(8,5))
    ax.plot(x_vals, y_vals)
    ax.set_title('f(x) = ' + sinartisi)
    ax.set_xlabel('Άξονας X')
    ax.set_ylabel('Άξονας Y')
    ax.grid(True)
    
    for i in lisi:
        if f(i) > 0:
            print('\n > Ελάχιστο: y* =', sinar(i),'\n             x* =',i)
            ax.annotate("Ελάχιστο",xytext=(i,i+20),xy=(i,sinar(i)), arrowprops={'facecolor':'black'})

        else:
            print('\n > Μέγιστο: y* =',sinar(i),'\n            x* =',i)
            ax.annotate("Μέγιστο",xytext=(i,i+20),xy=(i,sinar(i)), arrowprops={'facecolor':'black'})
    plt.show()
    
import os
os.system('cls' if os.name == 'nt' else 'clear')
print('')
print('______________________________________________________________________________________')
print('')
print('  Agricultural University of Athens')
print('  School of Applied Economics & Social Sciences')
print('  Department Of Agricultural Economics & Rural Development')
print('  Stefanos Stavrianos, UGRD')
print('  stefanos.stavrianos@outlook.com')
print('  +30 698 595 5584')
print('______________________________________________________________________________________')
print('')
print('                  __________________________________________________')
print('                 |                                                  |')
print('                 |         Α Κ Ρ Ο Τ Α Τ Α  Μ Ε  P Y T H O N        |')
print('                 |__________________________________________________|')

sinartisi = input('\n Συνάρτηση: f(x) = ')
while sinartisi == '':
    os.system('cls')
    print('')
    print('______________________________________________________________________________________')
    print('')
    print('  Agricultural University of Athens')
    print('  School of Applied Economics & Social Sciences')
    print('  Department Of Agricultural Economics & Rural Development')
    print('  Stefanos Stavrianos, UGRD')
    print('  stefanos.stavrianos@outlook.com')
    print('  +30 698 595 5584')
    print('______________________________________________________________________________________')
    print('')
    print('                  __________________________________________________')
    print('                 |                                                  |')
    print('                 |         Α Κ Ρ Ο Τ Α Τ Α  Μ Ε  P Y T H O N        |')
    print('                 |__________________________________________________|')
    print('')
    print('\n Μη έγκυρη καταχώρηση!')
    sinartisi = input('\n Συνάρτηση: f(x) = ')
megisto(sinartisi)
